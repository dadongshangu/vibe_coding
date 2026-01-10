"""
Flask 博客应用主程序
提供 RESTful API 和前端页面
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from database import init_database, get_connection, dict_factory
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)  # 允许跨域请求

# 初始化数据库
if not os.path.exists('blog.db'):
    init_database()


@app.route('/')
def index():
    """首页"""
    return render_template('index.html')


@app.route('/post/<int:post_id>')
def post_detail(post_id):
    """文章详情页"""
    return render_template('post.html', post_id=post_id)


@app.route('/editor')
@app.route('/editor/<int:post_id>')
def editor(post_id=None):
    """文章编辑器"""
    return render_template('editor.html', post_id=post_id)


# ========== API 端点 ==========

@app.route('/api/posts', methods=['GET'])
def get_posts():
    """获取所有文章（支持分页和搜索）"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    search = request.args.get('search', '', type=str)
    category = request.args.get('category', '', type=str)
    
    conn = get_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    
    # 构建查询条件
    where_clauses = []
    params = []
    
    if search:
        where_clauses.append("(title LIKE ? OR content LIKE ?)")
        search_term = f'%{search}%'
        params.extend([search_term, search_term])
    
    if category:
        where_clauses.append("category = ?")
        params.append(category)
    
    where_sql = " AND ".join(where_clauses) if where_clauses else "1=1"
    
    # 获取总数
    count_sql = f"SELECT COUNT(*) as total FROM posts WHERE {where_sql}"
    cursor.execute(count_sql, params)
    total = cursor.fetchone()['total']
    
    # 获取分页数据
    offset = (page - 1) * per_page
    sql = f"""
        SELECT * FROM posts 
        WHERE {where_sql}
        ORDER BY created_at DESC 
        LIMIT ? OFFSET ?
    """
    params.extend([per_page, offset])
    cursor.execute(sql, params)
    posts = cursor.fetchall()
    
    conn.close()
    
    return jsonify({
        'posts': posts,
        'total': total,
        'page': page,
        'per_page': per_page,
        'pages': (total + per_page - 1) // per_page
    })


@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    """获取单篇文章"""
    conn = get_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM posts WHERE id = ?', (post_id,))
    post = cursor.fetchone()
    
    conn.close()
    
    if post:
        return jsonify(post)
    else:
        return jsonify({'error': '文章不存在'}), 404


@app.route('/api/posts', methods=['POST'])
def create_post():
    """创建新文章"""
    data = request.get_json()
    
    if not data or not data.get('title') or not data.get('content'):
        return jsonify({'error': '标题和内容不能为空'}), 400
    
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO posts (title, content, category, tags, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        data.get('title'),
        data.get('content'),
        data.get('category', ''),
        data.get('tags', ''),
        now,
        now
    ))
    
    post_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return jsonify({'id': post_id, 'message': '文章创建成功'}), 201


@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    """更新文章"""
    data = request.get_json()
    
    conn = get_connection()
    cursor = conn.cursor()
    
    # 检查文章是否存在
    cursor.execute('SELECT id FROM posts WHERE id = ?', (post_id,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({'error': '文章不存在'}), 404
    
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 更新文章
    cursor.execute('''
        UPDATE posts 
        SET title = ?, content = ?, category = ?, tags = ?, updated_at = ?
        WHERE id = ?
    ''', (
        data.get('title'),
        data.get('content'),
        data.get('category', ''),
        data.get('tags', ''),
        now,
        post_id
    ))
    
    conn.commit()
    conn.close()
    
    return jsonify({'message': '文章更新成功'})


@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    """删除文章"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # 检查文章是否存在
    cursor.execute('SELECT id FROM posts WHERE id = ?', (post_id,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({'error': '文章不存在'}), 404
    
    cursor.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    conn.commit()
    conn.close()
    
    return jsonify({'message': '文章删除成功'})


@app.route('/api/categories', methods=['GET'])
def get_categories():
    """获取所有分类"""
    conn = get_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM categories ORDER BY name')
    categories = cursor.fetchall()
    
    conn.close()
    
    return jsonify(categories)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
