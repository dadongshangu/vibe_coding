"""
简单的待办事项应用
使用 Vibe Coding 方法创建
"""

import json
import os
from datetime import datetime
from typing import List, Dict

# 数据文件路径
DATA_FILE = "todos.json"


def load_todos() -> List[Dict]:
    """从 JSON 文件加载待办事项"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []


def save_todos(todos: List[Dict]) -> None:
    """保存待办事项到 JSON 文件"""
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(todos, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"保存文件时出错: {e}")


def add_todo(todos: List[Dict], task: str) -> None:
    """添加新的待办事项"""
    new_todo = {
        "id": len(todos) + 1,
        "task": task,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    todos.append(new_todo)
    save_todos(todos)
    print(f"✅ 已添加任务: {task}")


def display_todos(todos: List[Dict]) -> None:
    """显示所有待办事项"""
    if not todos:
        print("📝 暂无待办事项")
        return
    
    print("\n📋 待办事项列表:")
    print("-" * 50)
    for todo in todos:
        status = "✅" if todo["completed"] else "⏳"
        print(f"{status} [{todo['id']}] {todo['task']}")
        print(f"   创建时间: {todo['created_at']}")
    print("-" * 50)
    
    # 显示统计信息
    completed_count = sum(1 for todo in todos if todo["completed"])
    total_count = len(todos)
    print(f"\n📊 统计: {completed_count}/{total_count} 已完成")


def complete_todo(todos: List[Dict], todo_id: int) -> None:
    """标记任务为完成"""
    for todo in todos:
        if todo["id"] == todo_id:
            if todo["completed"]:
                print(f"⚠️  任务 [{todo_id}] 已经完成了")
            else:
                todo["completed"] = True
                save_todos(todos)
                print(f"✅ 任务 [{todo_id}] 已完成")
            return
    print(f"❌ 未找到 ID 为 {todo_id} 的任务")


def delete_todo(todos: List[Dict], todo_id: int) -> None:
    """删除待办事项"""
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            deleted_task = todos.pop(i)
            # 重新分配 ID
            for j, t in enumerate(todos, start=1):
                t["id"] = j
            save_todos(todos)
            print(f"🗑️  已删除任务: {deleted_task['task']}")
            return
    print(f"❌ 未找到 ID 为 {todo_id} 的任务")


def show_menu() -> None:
    """显示菜单"""
    print("\n" + "=" * 50)
    print("📝 待办事项管理器")
    print("=" * 50)
    print("1. 添加任务")
    print("2. 查看所有任务")
    print("3. 标记任务为完成")
    print("4. 删除任务")
    print("5. 退出")
    print("=" * 50)


def main():
    """主函数"""
    todos = load_todos()
    
    print("🎉 欢迎使用待办事项管理器！")
    
    while True:
        show_menu()
        choice = input("\n请选择操作 (1-5): ").strip()
        
        if choice == "1":
            task = input("请输入任务内容: ").strip()
            if task:
                add_todo(todos, task)
            else:
                print("❌ 任务内容不能为空")
        
        elif choice == "2":
            display_todos(todos)
        
        elif choice == "3":
            display_todos(todos)
            try:
                todo_id = int(input("\n请输入要完成的任务 ID: ").strip())
                complete_todo(todos, todo_id)
            except ValueError:
                print("❌ 请输入有效的数字 ID")
        
        elif choice == "4":
            display_todos(todos)
            try:
                todo_id = int(input("\n请输入要删除的任务 ID: ").strip())
                confirm = input(f"确定要删除任务 [{todo_id}] 吗？(y/n): ").strip().lower()
                if confirm == 'y':
                    delete_todo(todos, todo_id)
                else:
                    print("❌ 已取消删除")
            except ValueError:
                print("❌ 请输入有效的数字 ID")
        
        elif choice == "5":
            print("👋 再见！")
            break
        
        else:
            print("❌ 无效的选择，请输入 1-5")


if __name__ == "__main__":
    main()
