"""
数据库操作模块
负责数据库的初始化和基本操作
"""

import sqlite3
from datetime import datetime
from typing import List, Dict, Optional


def init_database():
    """初始化数据库，创建表结构"""
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    
    # 创建文章表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            category TEXT,
            tags TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
    ''')
    
    # 创建分类表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    ''')
    
    # 插入示例分类
    categories = ['技术', '生活', '旅行', '读书', '思考']
    for cat in categories:
        cursor.execute('INSERT OR IGNORE INTO categories (name) VALUES (?)', (cat,))
    
    # 插入示例文章（如果表为空）
    cursor.execute('SELECT COUNT(*) FROM posts')
    if cursor.fetchone()[0] == 0:
        sample_posts = [
            ('欢迎来到我的博客', 
             '这是我的第一篇博客文章。在这里我会分享技术心得、生活感悟和读书笔记。', 
             '生活', 
             '博客,介绍'),
            ('Python Flask 入门指南', 
             'Flask 是一个轻量级的 Python Web 框架，非常适合快速开发 Web 应用。本文将介绍 Flask 的基础用法。', 
             '技术', 
             'Python,Flask,Web开发'),
            ('如何提高编程效率', 
             '编程效率的提高需要多方面的努力：选择合适的工具、建立良好的习惯、持续学习新技术。', 
             '技术', 
             '编程,效率,技巧')
        ]
        
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for title, content, category, tags in sample_posts:
            cursor.execute('''
                INSERT INTO posts (title, content, category, tags, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (title, content, category, tags, now, now))
    
    conn.commit()
    conn.close()
    print("✅ 数据库初始化完成")


def get_connection():
    """获取数据库连接"""
    return sqlite3.connect('blog.db')


def dict_factory(cursor, row):
    """将查询结果转换为字典"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


if __name__ == '__main__':
    init_database()
