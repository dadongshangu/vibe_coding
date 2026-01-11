"""
Flask REST API 服务主程序
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from database import init_database, get_connection, dict_factory
from models import User, Product
from auth import register_user, authenticate_user, login_required, get_current_user
from validators import (
    validate_email, validate_username, validate_password,
    validate_product_data, sanitize_string
)
from config import Config
from datetime import datetime
import os

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, origins=Config.CORS_ORIGINS)

# 初始化数据库
if not os.path.exists(Config.DATABASE_PATH):
    init_database()


# ========== 辅助函数 ==========

def success_response(data=None, message='操作成功', status_code=200):
    """成功响应"""
    response = {'success': True, 'message': message}
    if data is not None:
        response['data'] = data
    return jsonify(response), status_code


def error_response(message='操作失败', status_code=400, errors=None):
    """错误响应"""
    response = {'success': False, 'error': message}
    if errors:
        response['errors'] = errors
    return jsonify(response), status_code


# ========== 认证端点 ==========

@app.route('/api/auth/register', methods=['POST'])
def register():
    """用户注册"""
    data = request.get_json()
    
    if not data:
        return error_response('请求数据不能为空', 400)
    
    username = data.get('username', '').strip()
    email = data.get('email', '').strip()
    password = data.get('password', '')
    
    # 验证输入
    is_valid, error = validate_username(username)
    if not is_valid:
        return error_response(error, 400)
    
    if not validate_email(email):
        return error_response('邮箱格式不正确', 400)
    
    is_valid, error = validate_password(password)
    if not is_valid:
        return error_response(error, 400)
    
    # 注册用户
    result = register_user(username, email, password)
    if 'error' in result:
        return error_response(result['error'], 400)
    
    return success_response(
        {'user': result},
        '用户注册成功',
        201
    )


@app.route('/api/auth/login', methods=['POST'])
def login():
    """用户登录"""
    data = request.get_json()
    
    if not data:
        return error_response('请求数据不能为空', 400)
    
    username = data.get('username', '').strip()
    password = data.get('password', '')
    
    if not username or not password:
        return error_response('用户名和密码不能为空', 400)
    
    # 验证用户
    result = authenticate_user(username, password)
    if 'error' in result:
        return error_response(result['error'], 401)
    
    return success_response(
        result,
        '登录成功'
    )


# ========== 产品端点 ==========

@app.route('/api/products', methods=['GET'])
@login_required
def get_products():
    """获取产品列表（支持分页和筛选）"""
    # 获取查询参数
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', Config.DEFAULT_PAGE_SIZE, type=int), Config.MAX_PAGE_SIZE)
    category = request.args.get('category', '')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    search = request.args.get('search', '')
    
    conn = get_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    
    # 构建查询条件
    where_clauses = []
    params = []
    
    if category:
        where_clauses.append("category = ?")
        params.append(category)
    
    if min_price is not None:
        where_clauses.append("price >= ?")
        params.append(min_price)
    
    if max_price is not None:
        where_clauses.append("price <= ?")
        params.append(max_price)
    
    if search:
        where_clauses.append("(name LIKE ? OR description LIKE ?)")
        search_term = f'%{search}%'
        params.extend([search_term, search_term])
    
    where_sql = " AND ".join(where_clauses) if where_clauses else "1=1"
    
    # 获取总数
    count_sql = f"SELECT COUNT(*) as total FROM products WHERE {where_sql}"
    cursor.execute(count_sql, params)
    total = cursor.fetchone()['total']
    
    # 获取分页数据
    offset = (page - 1) * per_page
    sql = f"""
        SELECT * FROM products 
        WHERE {where_sql}
        ORDER BY created_at DESC 
        LIMIT ? OFFSET ?
    """
    params.extend([per_page, offset])
    cursor.execute(sql, params)
    products = cursor.fetchall()
    
    conn.close()
    
    return success_response({
        'products': products,
        'total': total,
        'page': page,
        'per_page': per_page,
        'pages': (total + per_page - 1) // per_page
    })


@app.route('/api/products/<int:product_id>', methods=['GET'])
@login_required
def get_product(product_id):
    """获取单个产品"""
    conn = get_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    product = cursor.fetchone()
    
    conn.close()
    
    if product:
        return success_response(product)
    else:
        return error_response('产品不存在', 404)


@app.route('/api/products', methods=['POST'])
@login_required
def create_product():
    """创建新产品"""
    data = request.get_json()
    
    if not data:
        return error_response('请求数据不能为空', 400)
    
    # 验证数据
    errors = validate_product_data(data)
    if errors:
        return error_response('数据验证失败', 400, errors)
    
    # 清理输入
    name = sanitize_string(data.get('name', ''), 200)
    description = sanitize_string(data.get('description', ''), 2000)
    category = sanitize_string(data.get('category', ''), 100)
    
    price = float(data.get('price', 0))
    stock = int(data.get('stock', 0))
    
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user = get_current_user()
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO products (name, description, price, category, stock, created_by, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, description, price, category, stock, user['id'], now, now))
    
    product_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return success_response(
        {'id': product_id},
        '产品创建成功',
        201
    )


@app.route('/api/products/<int:product_id>', methods=['PUT'])
@login_required
def update_product(product_id):
    """更新产品"""
    data = request.get_json()
    
    if not data:
        return error_response('请求数据不能为空', 400)
    
    conn = get_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    
    # 检查产品是否存在
    cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    existing_product = cursor.fetchone()
    
    if not existing_product:
        conn.close()
        return error_response('产品不存在', 404)
    
    # 合并更新数据
    updated_data = {**existing_product, **data}
    errors = validate_product_data(updated_data)
    if errors:
        conn.close()
        return error_response('数据验证失败', 400, errors)
    
    # 更新字段
    name = sanitize_string(data.get('name', existing_product['name']), 200)
    description = sanitize_string(data.get('description', existing_product['description']), 2000)
    category = sanitize_string(data.get('category', existing_product['category']), 100)
    price = float(data.get('price', existing_product['price']))
    stock = int(data.get('stock', existing_product['stock']))
    
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute('''
        UPDATE products 
        SET name = ?, description = ?, price = ?, category = ?, stock = ?, updated_at = ?
        WHERE id = ?
    ''', (name, description, price, category, stock, now, product_id))
    
    conn.commit()
    conn.close()
    
    return success_response(message='产品更新成功')


@app.route('/api/products/<int:product_id>', methods=['DELETE'])
@login_required
def delete_product(product_id):
    """删除产品"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # 检查产品是否存在
    cursor.execute('SELECT id FROM products WHERE id = ?', (product_id,))
    if not cursor.fetchone():
        conn.close()
        return error_response('产品不存在', 404)
    
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()
    
    return success_response(message='产品删除成功')


# ========== 健康检查 ==========

@app.route('/api/health', methods=['GET'])
def health_check():
    """健康检查端点"""
    return success_response({'status': 'healthy'}, '服务运行正常')


# ========== 错误处理 ==========

@app.errorhandler(404)
def not_found(error):
    return error_response('资源不存在', 404)


@app.errorhandler(500)
def internal_error(error):
    return error_response('服务器内部错误', 500)


if __name__ == '__main__':
    app.run(debug=Config.DEBUG, host='0.0.0.0', port=5000)
