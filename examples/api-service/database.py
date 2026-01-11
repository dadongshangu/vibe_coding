"""
数据库操作模块
负责数据库的初始化和基本操作
"""

import sqlite3
from datetime import datetime
from typing import List, Dict, Optional
from config import Config


def init_database():
    """初始化数据库，创建表结构"""
    conn = sqlite3.connect(Config.DATABASE_PATH)
    cursor = conn.cursor()
    
    # 创建用户表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')
    
    # 创建产品表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            category TEXT,
            stock INTEGER DEFAULT 0,
            created_by INTEGER,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            FOREIGN KEY (created_by) REFERENCES users(id)
        )
    ''')
    
    # 创建索引
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_user_username ON users(username)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_user_email ON users(email)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_product_category ON products(category)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_product_created_by ON products(created_by)')
    
    conn.commit()
    conn.close()
    print("✅ 数据库初始化完成")


def get_connection():
    """获取数据库连接"""
    return sqlite3.connect(Config.DATABASE_PATH)


def dict_factory(cursor, row):
    """将查询结果转换为字典"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


if __name__ == '__main__':
    init_database()
