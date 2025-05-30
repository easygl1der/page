# 🎓 学术主页 / Academic Homepage

一个基于 Django 的个人学术主页项目，支持中英文双语，可以一键生成静态网站并部署到 GitHub Pages。

A Django-based personal academic homepage project with bilingual support (Chinese/English), featuring one-click static site generation and GitHub Pages deployment.

## ✨ 特性 / Features

- 🌐 **双语支持** / Bilingual Support (中文/English)
- 🎨 **现代化设计** / Modern Design with responsive layout
- 🌙 **主题切换** / Dark/Light theme toggle
- 📱 **响应式布局** / Mobile-friendly responsive design
- 🚀 **一键部署** / One-click deployment to GitHub Pages
- 📄 **静态网站生成** / Static site generation
- 🔧 **自动化构建** / Automated build process

## 📋 功能模块 / Modules

- **个人简介** / Personal Bio
- **研究兴趣** / Research Interests
- **教育背景** / Education
- **讲座分享** / Talks & Presentations
- **项目展示** / Projects
- **获奖经历** / Awards & Honors
- **个人爱好** / Hobbies
- **联系方式** / Contact Information

## 🛠️ 技术栈 / Tech Stack

- **后端** / Backend: Django 5.0.2
- **前端** / Frontend: HTML5, CSS3, JavaScript
- **样式** / Styling: Custom CSS with CSS Variables
- **图标** / Icons: Font Awesome 6.0
- **静态网站生成** / Static Generation: django-distill
- **部署** / Deployment: GitHub Pages

## 📦 安装与设置 / Installation & Setup

### 1. 克隆项目 / Clone Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd academic_homepage
```

### 2. 安装依赖 / Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. 数据库迁移 / Database Migration

```bash
python manage.py migrate
```

### 4. 收集静态文件 / Collect Static Files

```bash
python manage.py collectstatic
```

## 🚀 使用方法 / Usage

### 开发模式 / Development Mode

启动开发服务器：
```bash
python manage.py runserver
```

访问 `http://127.0.0.1:8000` 查看网站。

### 一键生成静态网站 / One-Click Static Site Generation

使用自动化构建脚本：

```bash
python build_docs.py
```

这个脚本会自动执行以下操作：
- ✅ 安装所有依赖包
- ✅ 收集静态文件到 `staticfiles/`
- ✅ 生成中文版主页 (`docs/index.html`)
- ✅ 生成英文版主页 (`docs/index_en.html`)
- ✅ 复制所有静态资源到 `docs/static/`
- ✅ 清理并重建 `docs/` 目录

生成完成后，`docs/` 目录将包含完整的静态网站文件。

## 🌐 部署到 GitHub Pages / Deploy to GitHub Pages

### 1. 推送代码到 GitHub / Push to GitHub

```bash
git add .
git commit -m "Add complete bilingual static site"
git push origin main
```

### 2. 配置 GitHub Pages / Configure GitHub Pages

1. 进入 GitHub 仓库页面
2. 点击 **Settings** 标签页
3. 在左侧菜单中选择 **Pages**
4. 在 **Source** 部分：
   - 选择 **Deploy from a branch**
   - 选择 **main** 分支
   - 选择 **/ docs** 文件夹
5. 点击 **Save** 保存设置

### 3. 访问网站 / Access Website

几分钟后，GitHub 会提供一个网址：
```
https://your-username.github.io/your-repo-name/
```

## 📁 项目结构 / Project Structure

```
academic_homepage/
├── academic_homepage/          # Django 项目配置
│   ├── settings.py            # 项目设置
│   ├── urls.py               # URL 配置
│   └── distill.py            # 静态网站生成配置
├── homepage/                  # 主应用
│   ├── views.py              # 视图函数
│   └── urls.py               # 应用 URL 配置
├── templates/                 # Django 模板
│   ├── base.html             # 中文版基础模板
│   ├── base_en.html          # 英文版基础模板
│   ├── index.html            # 中文版主页模板
│   ├── index_en.html         # 英文版主页模板
│   └── ...                   # 其他页面模板
├── static/                    # 静态文件源码
│   ├── css/                  # 样式文件
│   ├── images/               # 图片文件
│   └── files/                # 文档文件
├── docs/                      # 生成的静态网站 (GitHub Pages)
│   ├── index.html            # 中文版主页
│   ├── index_en.html         # 英文版主页
│   └── static/               # 静态资源
├── build_docs.py             # 自动化构建脚本
├── requirements.txt          # Python 依赖
└── README.md                 # 项目说明
```

## 🎨 自定义内容 / Customization

### 修改个人信息 / Update Personal Information

1. **基本信息**：编辑 `templates/index.html` 和 `templates/index_en.html`
2. **照片**：替换 `static/images/profile.jpg`
3. **简历**：替换 `static/files/resume_yueyihua.pdf`
4. **样式**：修改 `static/css/style.css`

### 添加新页面 / Add New Pages

1. 在 `templates/` 中创建新模板
2. 在 `homepage/views.py` 中添加视图函数
3. 在 `homepage/urls.py` 中添加 URL 配置
4. 更新 `build_docs.py` 脚本以生成新页面

### 修改主题 / Theme Customization

编辑 `static/css/style.css` 中的 CSS 变量：

```css
:root {
    --bg-primary: #ffffff;
    --text-primary: #333333;
    --accent-color: #2b6cb0;
    /* 更多变量... */
}
```

## 🔧 开发工具 / Development Tools

### 自动化脚本 / Automation Scripts

- `build_docs.py` - 一键生成静态网站
- `manage.py` - Django 管理命令

### 有用的命令 / Useful Commands

```bash
# 创建超级用户
python manage.py createsuperuser

# 运行测试
python manage.py test

# 检查项目
python manage.py check

# 生成静态网站
python build_docs.py
```

## 📝 更新流程 / Update Workflow

1. **修改内容**：更新模板文件或静态资源
2. **生成静态网站**：运行 `python build_docs.py`
3. **提交更改**：
   ```bash
   git add .
   git commit -m "Update content"
   git push origin main
   ```
4. **自动部署**：GitHub Pages 会自动更新网站

## 🐛 故障排除 / Troubleshooting

### 常见问题 / Common Issues

1. **静态文件不显示**
   - 确保运行了 `python manage.py collectstatic`
   - 检查 `STATIC_ROOT` 设置

2. **GitHub Pages 不更新**
   - 确保推送了 `docs/` 目录
   - 检查 GitHub Pages 设置是否正确

3. **样式不生效**
   - 清除浏览器缓存
   - 检查 CSS 文件路径

### 获取帮助 / Get Help

如果遇到问题，请：
1. 检查控制台错误信息
2. 查看 GitHub Pages 构建日志
3. 提交 Issue 到项目仓库

## 📄 许可证 / License

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 🤝 贡献 / Contributing

欢迎提交 Pull Request 或 Issue！

## 📞 联系方式 / Contact

- **邮箱** / Email: yueyh@mail2.sysu.edu.cn
- **GitHub**: https://github.com/easygl1der
- **网站** / Website: https://easygl1der.github.io/page/

---

⭐ 如果这个项目对你有帮助，请给它一个星标！

⭐ If this project helps you, please give it a star! 