// 全局变量
let currentPage = 1;
let currentSearch = '';
let currentCategory = '';

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', function() {
    // 根据当前页面执行不同操作
    const path = window.location.pathname;
    
    if (path === '/' || path === '/index.html') {
        initHomePage();
    } else if (path.startsWith('/post/')) {
        initPostDetail();
    } else if (path.startsWith('/editor')) {
        initEditor();
    }
});

// ========== 首页功能 ==========

async function initHomePage() {
    await loadCategories();
    loadPosts();
    
    // 搜索功能
    const searchInput = document.getElementById('searchInput');
    const categoryFilter = document.getElementById('categoryFilter');
    
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            loadPosts();
        }
    });
    
    categoryFilter.addEventListener('change', function() {
        currentCategory = this.value;
        currentPage = 1;
        loadPosts();
    });
}

async function loadCategories() {
    try {
        const response = await fetch('/api/categories');
        const categories = await response.json();
        
        const select = document.getElementById('categoryFilter');
        categories.forEach(cat => {
            const option = document.createElement('option');
            option.value = cat.name;
            option.textContent = cat.name;
            select.appendChild(option);
        });
    } catch (error) {
        console.error('加载分类失败:', error);
    }
}

async function loadPosts() {
    const searchInput = document.getElementById('searchInput');
    currentSearch = searchInput ? searchInput.value : '';
    
    const container = document.getElementById('postsContainer');
    container.innerHTML = '<div class="loading">加载中...</div>';
    
    try {
        const params = new URLSearchParams({
            page: currentPage,
            per_page: 10,
            search: currentSearch,
            category: currentCategory
        });
        
        const response = await fetch(`/api/posts?${params}`);
        const data = await response.json();
        
        if (data.posts.length === 0) {
            container.innerHTML = '<div class="loading">暂无文章</div>';
            return;
        }
        
        container.innerHTML = '';
        data.posts.forEach(post => {
            const card = createPostCard(post);
            container.appendChild(card);
        });
        
        renderPagination(data);
    } catch (error) {
        container.innerHTML = `<div class="error">加载失败: ${error.message}</div>`;
    }
}

function createPostCard(post) {
    const card = document.createElement('div');
    card.className = 'post-card';
    card.onclick = () => window.location.href = `/post/${post.id}`;
    
    const tags = post.tags ? post.tags.split(',').map(t => t.trim()) : [];
    
    card.innerHTML = `
        <h2>${escapeHtml(post.title)}</h2>
        <div class="post-meta">
            <span>📅 ${post.created_at}</span>
            <span>📂 ${post.category || '未分类'}</span>
        </div>
        <div class="post-excerpt">${escapeHtml(post.content.substring(0, 150))}${post.content.length > 150 ? '...' : ''}</div>
        ${tags.length > 0 ? `
            <div class="post-tags">
                ${tags.map(tag => `<span class="tag">${escapeHtml(tag)}</span>`).join('')}
            </div>
        ` : ''}
    `;
    
    return card;
}

function renderPagination(data) {
    const pagination = document.getElementById('pagination');
    if (!pagination) return;
    
    pagination.innerHTML = '';
    
    const totalPages = data.pages;
    if (totalPages <= 1) return;
    
    // 上一页按钮
    const prevBtn = document.createElement('button');
    prevBtn.textContent = '上一页';
    prevBtn.disabled = currentPage === 1;
    prevBtn.onclick = () => {
        currentPage--;
        loadPosts();
    };
    pagination.appendChild(prevBtn);
    
    // 页码按钮
    for (let i = 1; i <= totalPages; i++) {
        if (i === 1 || i === totalPages || (i >= currentPage - 2 && i <= currentPage + 2)) {
            const btn = document.createElement('button');
            btn.textContent = i;
            btn.className = i === currentPage ? 'active' : '';
            btn.onclick = () => {
                currentPage = i;
                loadPosts();
            };
            pagination.appendChild(btn);
        } else if (i === currentPage - 3 || i === currentPage + 3) {
            const ellipsis = document.createElement('span');
            ellipsis.textContent = '...';
            ellipsis.style.padding = '0.5rem';
            pagination.appendChild(ellipsis);
        }
    }
    
    // 下一页按钮
    const nextBtn = document.createElement('button');
    nextBtn.textContent = '下一页';
    nextBtn.disabled = currentPage === totalPages;
    nextBtn.onclick = () => {
        currentPage++;
        loadPosts();
    };
    pagination.appendChild(nextBtn);
}

// ========== 文章详情页 ==========

async function initPostDetail() {
    const postId = window.postId;
    if (!postId) return;
    
    await loadPostDetail(postId);
}

async function loadPostDetail(postId) {
    const container = document.getElementById('postDetail');
    container.innerHTML = '<div class="loading">加载中...</div>';
    
    try {
        const response = await fetch(`/api/posts/${postId}`);
        if (!response.ok) {
            throw new Error('文章不存在');
        }
        
        const post = await response.json();
        
        const tags = post.tags ? post.tags.split(',').map(t => t.trim()) : [];
        
        container.innerHTML = `
            <h1>${escapeHtml(post.title)}</h1>
            <div class="post-meta">
                <span>📅 ${post.created_at}</span>
                <span>📂 ${post.category || '未分类'}</span>
                ${post.updated_at !== post.created_at ? `<span>🔄 更新于 ${post.updated_at}</span>` : ''}
            </div>
            ${tags.length > 0 ? `
                <div class="post-tags">
                    ${tags.map(tag => `<span class="tag">${escapeHtml(tag)}</span>`).join('')}
                </div>
            ` : ''}
            <div class="post-content">${escapeHtml(post.content).replace(/\n/g, '<br>')}</div>
            <div class="post-actions">
                <a href="/editor/${postId}" class="btn btn-primary">编辑</a>
                <button onclick="deletePost(${postId})" class="btn btn-danger">删除</button>
                <a href="/" class="btn btn-secondary">返回首页</a>
            </div>
        `;
    } catch (error) {
        container.innerHTML = `<div class="error">加载失败: ${error.message}</div>`;
    }
}

async function deletePost(postId) {
    if (!confirm('确定要删除这篇文章吗？')) {
        return;
    }
    
    try {
        const response = await fetch(`/api/posts/${postId}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            alert('文章删除成功');
            window.location.href = '/';
        } else {
            const data = await response.json();
            alert('删除失败: ' + data.error);
        }
    } catch (error) {
        alert('删除失败: ' + error.message);
    }
}

// ========== 编辑器功能 ==========

async function initEditor() {
    await loadCategories();
    
    const postId = window.postId;
    if (postId) {
        document.getElementById('editorTitle').textContent = '编辑文章';
        await loadPostForEdit(postId);
    }
    
    const form = document.getElementById('postForm');
    form.addEventListener('submit', handleSubmit);
}

async function loadCategories() {
    try {
        const response = await fetch('/api/categories');
        const categories = await response.json();
        
        const select = document.getElementById('category');
        categories.forEach(cat => {
            const option = document.createElement('option');
            option.value = cat.name;
            option.textContent = cat.name;
            select.appendChild(option);
        });
    } catch (error) {
        console.error('加载分类失败:', error);
    }
}

async function loadPostForEdit(postId) {
    try {
        const response = await fetch(`/api/posts/${postId}`);
        if (!response.ok) {
            throw new Error('文章不存在');
        }
        
        const post = await response.json();
        
        document.getElementById('title').value = post.title;
        document.getElementById('content').value = post.content;
        document.getElementById('category').value = post.category || '';
        document.getElementById('tags').value = post.tags || '';
    } catch (error) {
        alert('加载文章失败: ' + error.message);
        window.location.href = '/';
    }
}

async function handleSubmit(e) {
    e.preventDefault();
    
    const postId = window.postId;
    const data = {
        title: document.getElementById('title').value,
        content: document.getElementById('content').value,
        category: document.getElementById('category').value,
        tags: document.getElementById('tags').value
    };
    
    try {
        const url = postId ? `/api/posts/${postId}` : '/api/posts';
        const method = postId ? 'PUT' : 'POST';
        
        const response = await fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        if (response.ok) {
            const result = await response.json();
            alert(postId ? '文章更新成功' : '文章创建成功');
            if (postId) {
                window.location.href = `/post/${postId}`;
            } else {
                window.location.href = '/';
            }
        } else {
            const error = await response.json();
            alert('保存失败: ' + error.error);
        }
    } catch (error) {
        alert('保存失败: ' + error.message);
    }
}

// ========== 工具函数 ==========

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
