"""
数据模型定义
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    """用户数据模型"""
    id: Optional[int]
    username: str
    email: str
    password_hash: str
    created_at: str
    
    @classmethod
    def from_dict(cls, data: dict):
        """从字典创建 User 对象"""
        return cls(
            id=data.get('id'),
            username=data.get('username', ''),
            email=data.get('email', ''),
            password_hash=data.get('password_hash', ''),
            created_at=data.get('created_at', '')
        )
    
    def to_dict(self, include_password=False):
        """转换为字典"""
        data = {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at
        }
        if include_password:
            data['password_hash'] = self.password_hash
        return data


@dataclass
class Product:
    """产品数据模型"""
    id: Optional[int]
    name: str
    description: str
    price: float
    category: str
    stock: int
    created_by: Optional[int]
    created_at: str
    updated_at: str
    
    @classmethod
    def from_dict(cls, data: dict):
        """从字典创建 Product 对象"""
        return cls(
            id=data.get('id'),
            name=data.get('name', ''),
            description=data.get('description', ''),
            price=float(data.get('price', 0)),
            category=data.get('category', ''),
            stock=int(data.get('stock', 0)),
            created_by=data.get('created_by'),
            created_at=data.get('created_at', ''),
            updated_at=data.get('updated_at', '')
        )
    
    def to_dict(self):
        """转换为字典"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'category': self.category,
            'stock': self.stock,
            'created_by': self.created_by,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    def validate(self):
        """验证数据有效性"""
        errors = []
        
        if not self.name or not self.name.strip():
            errors.append('产品名称不能为空')
        
        if self.price < 0:
            errors.append('价格不能为负数')
        
        if self.stock < 0:
            errors.append('库存不能为负数')
        
        return errors
