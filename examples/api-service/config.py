"""
配置文件
"""

import os
from datetime import timedelta


class Config:
    """应用配置"""
    # Flask 配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    # 数据库配置
    DATABASE_PATH = 'api_service.db'
    
    # JWT 配置
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or SECRET_KEY
    JWT_ALGORITHM = 'HS256'
    JWT_EXPIRATION_DELTA = timedelta(days=7)
    
    # CORS 配置
    CORS_ORIGINS = ['*']  # 生产环境应限制具体域名
    
    # 分页配置
    DEFAULT_PAGE_SIZE = 10
    MAX_PAGE_SIZE = 100
