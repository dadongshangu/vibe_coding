"""
数据模型定义
定义任务的数据结构
"""

from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Task:
    """任务数据模型"""
    id: Optional[int]
    title: str
    description: str
    priority: str  # 高、中、低
    status: str  # 待办、进行中、已完成
    category: str
    due_date: Optional[str]
    created_at: str
    updated_at: str
    
    @classmethod
    def from_dict(cls, data: dict):
        """从字典创建 Task 对象"""
        return cls(
            id=data.get('id'),
            title=data.get('title', ''),
            description=data.get('description', ''),
            priority=data.get('priority', '中'),
            status=data.get('status', '待办'),
            category=data.get('category', ''),
            due_date=data.get('due_date'),
            created_at=data.get('created_at', ''),
            updated_at=data.get('updated_at', '')
        )
    
    def to_dict(self):
        """转换为字典"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'status': self.status,
            'category': self.category,
            'due_date': self.due_date,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    def validate(self):
        """验证数据有效性"""
        errors = []
        
        if not self.title or not self.title.strip():
            errors.append('标题不能为空')
        
        if self.priority not in ['高', '中', '低']:
            errors.append('优先级必须是：高、中、低')
        
        if self.status not in ['待办', '进行中', '已完成']:
            errors.append('状态必须是：待办、进行中、已完成')
        
        return errors
