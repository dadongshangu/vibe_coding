"""
数据库操作模块
负责数据库的初始化和基本操作
"""

import sqlite3
from datetime import datetime
from typing import List, Dict, Optional


def init_database():
    """初始化数据库，创建表结构"""
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    
    # 创建任务表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            priority TEXT NOT NULL DEFAULT '中',
            status TEXT NOT NULL DEFAULT '待办',
            category TEXT,
            due_date TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
    ''')
    
    # 创建索引以提高查询性能
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_status ON tasks(status)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_priority ON tasks(priority)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_category ON tasks(category)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_due_date ON tasks(due_date)')
    
    # 插入示例任务（如果表为空）
    cursor.execute('SELECT COUNT(*) FROM tasks')
    if cursor.fetchone()[0] == 0:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sample_tasks = [
            ('完成项目文档', '编写项目 README 和 API 文档', '高', '进行中', '工作', '2024-12-31', now, now),
            ('学习 Flask', '深入学习 Flask 框架的高级特性', '中', '待办', '学习', '2024-12-25', now, now),
            ('锻炼身体', '每天跑步 30 分钟', '中', '待办', '健康', None, now, now),
            ('阅读《Python 编程》', '阅读第 5-8 章', '低', '已完成', '学习', '2024-12-20', now, now),
            ('准备会议材料', '准备下周项目评审会议的材料', '高', '待办', '工作', '2024-12-28', now, now),
        ]
        
        cursor.executemany('''
            INSERT INTO tasks (title, description, priority, status, category, due_date, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', sample_tasks)
    
    conn.commit()
    conn.close()
    print("✅ 数据库初始化完成")


def get_connection():
    """获取数据库连接"""
    return sqlite3.connect('tasks.db')


def dict_factory(cursor, row):
    """将查询结果转换为字典"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


if __name__ == '__main__':
    init_database()
