// 全局变量
let currentTasks = [];
let categories = new Set();

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', function() {
    const path = window.location.pathname;
    
    if (path === '/' || path === '/index.html') {
        initTaskList();
    } else if (path === '/stats') {
        initStats();
    }
});

// ========== 任务列表页面 ==========

async function initTaskList() {
    await loadTasks();
    loadCategories();
    
    // 表单提交
    const form = document.getElementById('taskForm');
    if (form) {
        form.addEventListener('submit', handleTaskSubmit);
    }
}

async function loadTasks() {
    const container = document.getElementById('tasksContainer');
    if (!container) return;
    
    container.innerHTML = '<div class="loading">加载中...</div>';
    
    try {
        const params = buildQueryParams();
        const response = await fetch(`/api/tasks?${params}`);
        const tasks = await response.json();
        
        currentTasks = tasks;
        
        if (tasks.length === 0) {
            container.innerHTML = '<div class="loading">暂无任务</div>';
            return;
        }
        
        container.innerHTML = '';
        tasks.forEach(task => {
            const card = createTaskCard(task);
            container.appendChild(card);
        });
        
        // 更新分类选项
        updateCategoryFilter();
    } catch (error) {
        container.innerHTML = `<div class="error">加载失败: ${error.message}</div>`;
    }
}

function buildQueryParams() {
    const params = new URLSearchParams();
    
    const status = document.getElementById('statusFilter')?.value;
    const priority = document.getElementById('priorityFilter')?.value;
    const category = document.getElementById('categoryFilter')?.value;
    const search = document.getElementById('searchInput')?.value;
    const sort = document.getElementById('sortSelect')?.value;
    
    if (status) params.append('status', status);
    if (priority) params.append('priority', priority);
    if (category) params.append('category', category);
    if (search) params.append('search', search);
    
    if (sort) {
        const [field, order] = sort.split('-');
        params.append('sort', field);
        params.append('order', order);
    }
    
    return params.toString();
}

function applyFilters() {
    loadTasks();
}

function loadCategories() {
    currentTasks.forEach(task => {
        if (task.category) {
            categories.add(task.category);
        }
    });
    updateCategoryFilter();
}

function updateCategoryFilter() {
    const filter = document.getElementById('categoryFilter');
    if (!filter) return;
    
    // 保存当前选择
    const currentValue = filter.value;
    
    // 清空选项（保留"所有分类"）
    filter.innerHTML = '<option value="">所有分类</option>';
    
    // 添加分类选项
    Array.from(categories).sort().forEach(cat => {
        const option = document.createElement('option');
        option.value = cat;
        option.textContent = cat;
        if (cat === currentValue) {
            option.selected = true;
        }
        filter.appendChild(option);
    });
}

function createTaskCard(task) {
    const card = document.createElement('div');
    card.className = `task-card ${task.status === '已完成' ? 'completed' : ''}`;
    
    const priorityClass = `priority-${task.priority === '高' ? 'high' : task.priority === '中' ? 'medium' : 'low'}`;
    
    card.innerHTML = `
        <div class="task-header">
            <div class="task-title">${escapeHtml(task.title)}</div>
            <span class="task-priority ${priorityClass}">${task.priority}</span>
        </div>
        ${task.description ? `<div class="task-description">${escapeHtml(task.description)}</div>` : ''}
        <div class="task-meta">
            <span class="task-status status-${task.status}">${task.status}</span>
            ${task.category ? `<span>📂 ${escapeHtml(task.category)}</span>` : ''}
            ${task.due_date ? `<span>📅 ${task.due_date}</span>` : ''}
            <span>🕐 ${task.created_at}</span>
        </div>
        <div class="task-actions">
            ${task.status !== '已完成' ? `
                <button class="btn-complete" onclick="completeTask(${task.id})">完成</button>
            ` : ''}
            <button class="btn-edit" onclick="editTask(${task.id})">编辑</button>
            <button class="btn-delete" onclick="deleteTask(${task.id})">删除</button>
        </div>
    `;
    
    return card;
}

// ========== 任务操作 ==========

function showTaskForm(taskId = null) {
    const modal = document.getElementById('taskModal');
    const form = document.getElementById('taskForm');
    const title = document.getElementById('modalTitle');
    
    if (taskId) {
        title.textContent = '编辑任务';
        loadTaskForEdit(taskId);
    } else {
        title.textContent = '新建任务';
        form.reset();
        document.getElementById('taskId').value = '';
    }
    
    modal.style.display = 'block';
}

function closeTaskForm() {
    const modal = document.getElementById('taskModal');
    modal.style.display = 'none';
}

async function loadTaskForEdit(taskId) {
    try {
        const response = await fetch(`/api/tasks/${taskId}`);
        if (!response.ok) {
            throw new Error('任务不存在');
        }
        
        const task = await response.json();
        
        document.getElementById('taskId').value = task.id;
        document.getElementById('title').value = task.title;
        document.getElementById('description').value = task.description || '';
        document.getElementById('priority').value = task.priority;
        document.getElementById('status').value = task.status;
        document.getElementById('category').value = task.category || '';
        document.getElementById('dueDate').value = task.due_date || '';
    } catch (error) {
        alert('加载任务失败: ' + error.message);
        closeTaskForm();
    }
}

async function handleTaskSubmit(e) {
    e.preventDefault();
    
    const taskId = document.getElementById('taskId').value;
    const data = {
        title: document.getElementById('title').value,
        description: document.getElementById('description').value,
        priority: document.getElementById('priority').value,
        status: document.getElementById('status').value,
        category: document.getElementById('category').value,
        due_date: document.getElementById('dueDate').value || null
    };
    
    try {
        const url = taskId ? `/api/tasks/${taskId}` : '/api/tasks';
        const method = taskId ? 'PUT' : 'POST';
        
        const response = await fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        if (response.ok) {
            alert(taskId ? '任务更新成功' : '任务创建成功');
            closeTaskForm();
            loadTasks();
        } else {
            const error = await response.json();
            alert('保存失败: ' + error.error);
        }
    } catch (error) {
        alert('保存失败: ' + error.message);
    }
}

async function editTask(taskId) {
    showTaskForm(taskId);
}

async function completeTask(taskId) {
    try {
        const response = await fetch(`/api/tasks/${taskId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ status: '已完成' })
        });
        
        if (response.ok) {
            loadTasks();
        } else {
            const error = await response.json();
            alert('操作失败: ' + error.error);
        }
    } catch (error) {
        alert('操作失败: ' + error.message);
    }
}

async function deleteTask(taskId) {
    if (!confirm('确定要删除这个任务吗？')) {
        return;
    }
    
    try {
        const response = await fetch(`/api/tasks/${taskId}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            loadTasks();
        } else {
            const error = await response.json();
            alert('删除失败: ' + error.error);
        }
    } catch (error) {
        alert('删除失败: ' + error.message);
    }
}

// ========== 统计页面 ==========

async function initStats() {
    await loadStats();
}

async function loadStats() {
    const container = document.getElementById('statsContent');
    if (!container) return;
    
    container.innerHTML = '<div class="loading">加载中...</div>';
    
    try {
        const response = await fetch('/api/stats');
        const stats = await response.json();
        
        container.innerHTML = `
            <div class="stat-grid">
                <div class="stat-item">
                    <div class="value">${stats.total}</div>
                    <div class="label">总任务数</div>
                </div>
                <div class="stat-item">
                    <div class="value">${stats.pending}</div>
                    <div class="label">待办</div>
                </div>
                <div class="stat-item">
                    <div class="value">${stats.in_progress}</div>
                    <div class="label">进行中</div>
                </div>
                <div class="stat-item">
                    <div class="value">${stats.completed}</div>
                    <div class="label">已完成</div>
                </div>
                <div class="stat-item">
                    <div class="value">${stats.upcoming}</div>
                    <div class="label">即将到期</div>
                </div>
            </div>
            
            <div class="stat-card">
                <h3>按优先级分布</h3>
                <div class="stat-grid">
                    ${Object.entries(stats.by_priority).map(([priority, count]) => `
                        <div class="stat-item">
                            <div class="value">${count}</div>
                            <div class="label">${priority}优先级</div>
                        </div>
                    `).join('')}
                </div>
            </div>
            
            ${Object.keys(stats.by_category).length > 0 ? `
                <div class="stat-card">
                    <h3>按分类分布</h3>
                    <div class="stat-grid">
                        ${Object.entries(stats.by_category).map(([category, count]) => `
                            <div class="stat-item">
                                <div class="value">${count}</div>
                                <div class="label">${category}</div>
                            </div>
                        `).join('')}
                    </div>
                </div>
            ` : ''}
        `;
    } catch (error) {
        container.innerHTML = `<div class="error">加载失败: ${error.message}</div>`;
    }
}

// ========== 工具函数 ==========

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// 点击模态框外部关闭
window.onclick = function(event) {
    const modal = document.getElementById('taskModal');
    if (event.target === modal) {
        closeTaskForm();
    }
}
