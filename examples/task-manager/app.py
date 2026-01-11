"""
Flask 任务管理应用主程序
提供 RESTful API 和前端页面
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from database import init_database, get_connection, dict_factory
from models import Task
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)  # 允许跨域请求

# 初始化数据库
if not os.path.exists('tasks.db'):
    init_database()


@app.route('/')
def index():
    """首页"""
    return render_template('index.html')


@app.route('/stats')
def stats():
    """统计页面"""
    return render_template('stats.html')


# ========== API 端点 ==========

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """获取所有任务（支持筛选、排序和搜索）"""
    # 获取查询参数
    status = request.args.get('status', '')
    priority = request.args.get('priority', '')
    category = request.args.get('category', '')
    search = request.args.get('search', '')
    sort = request.args.get('sort', 'created_at')
    order = request.args.get('order', 'desc')
    
    conn = get_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    
    # 构建查询条件
    where_clauses = []
    params = []
    
    if status:
        where_clauses.append("status = ?")
        params.append(status)
    
    if priority:
        where_clauses.append("priority = ?")
        params.append(priority)
    
    if category:
        where_clauses.append("category = ?")
        params.append(category)
    
    if search:
        where_clauses.append("(title LIKE ? OR description LIKE ?)")
        search_term = f'%{search}%'
        params.extend([search_term, search_term])
    
    where_sql = " AND ".join(where_clauses) if where_clauses else "1=1"
    
    # 验证排序字段
    valid_sort_fields = ['created_at', 'updated_at', 'due_date', 'priority', 'status', 'title']
    if sort not in valid_sort_fields:
        sort = 'created_at'
    
    # 验证排序方向
    order = 'DESC' if order.lower() == 'desc' else 'ASC'
    
    # 执行查询
    sql = f"""
        SELECT * FROM tasks 
        WHERE {where_sql}
        ORDER BY {sort} {order}
    """
    cursor.execute(sql, params)
    tasks = cursor.fetchall()
    
    conn.close()
    
    return jsonify(tasks)


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """获取单个任务"""
    conn = get_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task = cursor.fetchone()
    
    conn.close()
    
    if task:
        return jsonify(task)
    else:
        return jsonify({'error': '任务不存在'}), 404


@app.route('/api/tasks', methods=['POST'])
def create_task():
    """创建新任务"""
    data = request.get_json()
    
    if not data or not data.get('title'):
        return jsonify({'error': '标题不能为空'}), 400
    
    # 创建任务对象并验证
    task = Task.from_dict(data)
    errors = task.validate()
    if errors:
        return jsonify({'error': '; '.join(errors)}), 400
    
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO tasks (title, description, priority, status, category, due_date, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        task.title,
        task.description,
        task.priority,
        task.status,
        task.category,
        task.due_date,
        now,
        now
    ))
    
    task_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return jsonify({'id': task_id, 'message': '任务创建成功'}), 201


@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """更新任务"""
    data = request.get_json()
    
    conn = get_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    
    # 检查任务是否存在
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    existing_task = cursor.fetchone()
    
    if not existing_task:
        conn.close()
        return jsonify({'error': '任务不存在'}), 404
    
    # 合并更新数据
    updated_data = {**existing_task, **data}
    task = Task.from_dict(updated_data)
    
    # 验证数据
    errors = task.validate()
    if errors:
        conn.close()
        return jsonify({'error': '; '.join(errors)}), 400
    
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 更新任务
    cursor.execute('''
        UPDATE tasks 
        SET title = ?, description = ?, priority = ?, status = ?, 
            category = ?, due_date = ?, updated_at = ?
        WHERE id = ?
    ''', (
        task.title,
        task.description,
        task.priority,
        task.status,
        task.category,
        task.due_date,
        now,
        task_id
    ))
    
    conn.commit()
    conn.close()
    
    return jsonify({'message': '任务更新成功'})


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """删除任务"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # 检查任务是否存在
    cursor.execute('SELECT id FROM tasks WHERE id = ?', (task_id,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({'error': '任务不存在'}), 404
    
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    
    return jsonify({'message': '任务删除成功'})


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """获取任务统计信息"""
    conn = get_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    
    # 总数
    cursor.execute('SELECT COUNT(*) as total FROM tasks')
    total = cursor.fetchone()['total']
    
    # 按状态统计
    cursor.execute('''
        SELECT status, COUNT(*) as count 
        FROM tasks 
        GROUP BY status
    ''')
    status_stats = {row['status']: row['count'] for row in cursor.fetchall()}
    
    # 按优先级统计
    cursor.execute('''
        SELECT priority, COUNT(*) as count 
        FROM tasks 
        GROUP BY priority
    ''')
    priority_stats = {row['priority']: row['count'] for row in cursor.fetchall()}
    
    # 按分类统计
    cursor.execute('''
        SELECT category, COUNT(*) as count 
        FROM tasks 
        WHERE category IS NOT NULL AND category != ''
        GROUP BY category
    ''')
    category_stats = {row['category']: row['count'] for row in cursor.fetchall()}
    
    # 即将到期的任务（3天内）
    from datetime import datetime, timedelta
    three_days_later = (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
    cursor.execute('''
        SELECT COUNT(*) as count 
        FROM tasks 
        WHERE due_date IS NOT NULL 
        AND due_date <= ? 
        AND status != '已完成'
    ''', (three_days_later,))
    upcoming = cursor.fetchone()['count']
    
    conn.close()
    
    return jsonify({
        'total': total,
        'pending': status_stats.get('待办', 0),
        'in_progress': status_stats.get('进行中', 0),
        'completed': status_stats.get('已完成', 0),
        'by_priority': priority_stats,
        'by_category': category_stats,
        'upcoming': upcoming
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
