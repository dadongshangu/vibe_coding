"""
API 测试文件
使用 pytest 运行测试
"""

import pytest
import json
from app import app
from database import init_database, get_connection
import os


@pytest.fixture
def client():
    """测试客户端"""
    # 使用测试数据库
    app.config['DATABASE_PATH'] = 'test_api.db'
    
    # 初始化测试数据库
    if os.path.exists('test_api.db'):
        os.remove('test_api.db')
    init_database()
    
    with app.test_client() as client:
        yield client
    
    # 清理测试数据库
    if os.path.exists('test_api.db'):
        os.remove('test_api.db')


def test_health_check(client):
    """测试健康检查端点"""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] is True


def test_register_user(client):
    """测试用户注册"""
    response = client.post('/api/auth/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpass123'
    })
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['success'] is True
    assert 'user' in data['data']


def test_register_duplicate_username(client):
    """测试重复用户名注册"""
    # 第一次注册
    client.post('/api/auth/register', json={
        'username': 'testuser',
        'email': 'test1@example.com',
        'password': 'testpass123'
    })
    
    # 第二次注册相同用户名
    response = client.post('/api/auth/register', json={
        'username': 'testuser',
        'email': 'test2@example.com',
        'password': 'testpass123'
    })
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['success'] is False


def test_login(client):
    """测试用户登录"""
    # 先注册
    client.post('/api/auth/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpass123'
    })
    
    # 登录
    response = client.post('/api/auth/login', json={
        'username': 'testuser',
        'password': 'testpass123'
    })
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] is True
    assert 'token' in data['data']


def test_login_invalid_credentials(client):
    """测试无效凭据登录"""
    response = client.post('/api/auth/login', json={
        'username': 'nonexistent',
        'password': 'wrongpass'
    })
    
    assert response.status_code == 401
    data = json.loads(response.data)
    assert data['success'] is False


def test_create_product_requires_auth(client):
    """测试创建产品需要认证"""
    response = client.post('/api/products', json={
        'name': 'Test Product',
        'price': 99.99
    })
    
    assert response.status_code == 401


def test_create_product(client):
    """测试创建产品"""
    # 注册并登录
    client.post('/api/auth/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpass123'
    })
    
    login_response = client.post('/api/auth/login', json={
        'username': 'testuser',
        'password': 'testpass123'
    })
    token = json.loads(login_response.data)['data']['token']
    
    # 创建产品
    response = client.post('/api/products', 
        json={
            'name': 'Test Product',
            'description': 'Test Description',
            'price': 99.99,
            'category': 'Test',
            'stock': 10
        },
        headers={'Authorization': f'Bearer {token}'}
    )
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['success'] is True
    assert 'id' in data['data']


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
