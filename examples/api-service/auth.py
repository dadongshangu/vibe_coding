"""
认证模块
处理用户认证和 JWT 令牌
"""

import jwt
import bcrypt
from datetime import datetime, timedelta
from functools import wraps
from flask import request, jsonify
from config import Config
from database import get_connection, dict_factory


def hash_password(password: str) -> str:
    """加密密码"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def verify_password(password: str, password_hash: str) -> bool:
    """验证密码"""
    return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))


def generate_token(user_id: int, username: str) -> str:
    """生成 JWT 令牌"""
    payload = {
        'user_id': user_id,
        'username': username,
        'exp': datetime.utcnow() + Config.JWT_EXPIRATION_DELTA,
        'iat': datetime.utcnow()
    }
    return jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm=Config.JWT_ALGORITHM)


def verify_token(token: str) -> dict:
    """验证 JWT 令牌"""
    try:
        payload = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=[Config.JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def get_current_user():
    """从请求中获取当前用户"""
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return None
    
    try:
        token = auth_header.split(' ')[1]  # Bearer <token>
        payload = verify_token(token)
        if not payload:
            return None
        
        # 从数据库获取用户信息
        conn = get_connection()
        conn.row_factory = dict_factory
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE id = ?', (payload['user_id'],))
        user = cursor.fetchone()
        conn.close()
        
        return user
    except (IndexError, KeyError):
        return None


def login_required(f):
    """需要登录的装饰器"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = get_current_user()
        if not user:
            return jsonify({'error': '需要认证', 'message': '请提供有效的 JWT 令牌'}), 401
        request.current_user = user
        return f(*args, **kwargs)
    return decorated_function


def register_user(username: str, email: str, password: str) -> dict:
    """注册新用户"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # 检查用户名是否已存在
    cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
    if cursor.fetchone():
        conn.close()
        return {'error': '用户名已存在'}
    
    # 检查邮箱是否已存在
    cursor.execute('SELECT id FROM users WHERE email = ?', (email,))
    if cursor.fetchone():
        conn.close()
        return {'error': '邮箱已被注册'}
    
    # 创建新用户
    password_hash = hash_password(password)
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute('''
        INSERT INTO users (username, email, password_hash, created_at)
        VALUES (?, ?, ?, ?)
    ''', (username, email, password_hash, now))
    
    user_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return {'user_id': user_id, 'username': username, 'email': email}


def authenticate_user(username: str, password: str) -> dict:
    """验证用户登录"""
    conn = get_connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    
    if not user:
        return {'error': '用户名或密码错误'}
    
    if not verify_password(password, user['password_hash']):
        return {'error': '用户名或密码错误'}
    
    token = generate_token(user['id'], user['username'])
    
    return {
        'user': {
            'id': user['id'],
            'username': user['username'],
            'email': user['email']
        },
        'token': token
    }
