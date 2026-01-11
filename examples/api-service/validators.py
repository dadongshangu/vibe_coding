"""
数据验证模块
"""

import re
from typing import List, Optional, Tuple


def validate_email(email: str) -> bool:
    """验证邮箱格式"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_username(username: str) -> Tuple[bool, Optional[str]]:
    """验证用户名"""
    if not username or len(username.strip()) < 3:
        return False, '用户名至少需要 3 个字符'
    
    if len(username) > 20:
        return False, '用户名不能超过 20 个字符'
    
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return False, '用户名只能包含字母、数字和下划线'
    
    return True, None


def validate_password(password: str) -> Tuple[bool, Optional[str]]:
    """验证密码"""
    if not password or len(password) < 6:
        return False, '密码至少需要 6 个字符'
    
    if len(password) > 100:
        return False, '密码不能超过 100 个字符'
    
    return True, None


def validate_product_data(data: dict) -> List[str]:
    """验证产品数据"""
    errors = []
    
    if not data.get('name') or not data.get('name', '').strip():
        errors.append('产品名称不能为空')
    
    price = data.get('price')
    if price is None:
        errors.append('价格不能为空')
    else:
        try:
            price = float(price)
            if price < 0:
                errors.append('价格不能为负数')
        except (ValueError, TypeError):
            errors.append('价格必须是有效的数字')
    
    stock = data.get('stock')
    if stock is not None:
        try:
            stock = int(stock)
            if stock < 0:
                errors.append('库存不能为负数')
        except (ValueError, TypeError):
            errors.append('库存必须是有效的整数')
    
    return errors


def sanitize_string(value: str, max_length: int = 1000) -> str:
    """清理字符串输入"""
    if not value:
        return ''
    
    # 移除前后空格
    value = value.strip()
    
    # 限制长度
    if len(value) > max_length:
        value = value[:max_length]
    
    return value
