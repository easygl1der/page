# 🎓 乐绎华 - 学术主页 / Yue Yihua - Academic Homepage

一个基于 Django 的个人学术主页项目，支持中英文双语，具有现代化设计和主题切换功能，可以一键生成静态网站并部署到 GitHub Pages。

A Django-based personal academic homepage project with bilingual support (Chinese/English), featuring modern design, theme switching, one-click static site generation and GitHub Pages deployment.

🌐 **在线访问 / Live Demo**: [https://easygl1der.github.io/page/](https://easygl1der.github.io/page/)

## ✨ 特性 / Features

* 🌐 **双语支持** / Bilingual Support (中文/English)
* 🎨 **现代化设计** / Modern Design with responsive layout
* 🌙 **主题切换** / Dark/Light theme toggle  
* 📱 **响应式布局** / Mobile-friendly responsive design
* 🚀 **一键部署** / One-click deployment to GitHub Pages
* 📄 **静态网站生成** / Static site generation
* 🔧 **自动化构建** / Automated build process
* 💼 **简约导航栏** / Minimalist navigation bar
* 🎯 **交互式项目卡片** / Interactive project cards
* 📧 **联系方式集成** / Integrated contact methods (Email, GitHub, Telegram)

## 📋 功能模块 / Modules

* **个人简介** / Personal Bio with social links
* **讲座分享** / Talks & Presentations with detailed pages  
* **项目展示** / Projects (Mathematica研究项目等)
* **获奖经历** / Awards & Honors
* **技能专长** / Skills & Expertise
* **个人爱好** / Hobbies (足球等)
* **联系方式** / Contact Information

## 🛠️ 技术栈 / Tech Stack

* **后端** / Backend: Django 5.0.2
* **前端** / Frontend: HTML5, CSS3, JavaScript
* **样式** / Styling: Custom CSS with CSS Variables, Dark/Light theme
* **图标** / Icons: Font Awesome 5.15.4, Heroicons
* **静态网站生成** / Static Generation: django-distill, django-bakery
* **部署** / Deployment: GitHub Pages

## 📦 安装与设置 / Installation & Setup

### 1. 克隆项目 / Clone Repository

```bash
git clone https://github.com/easygl1der/page.git
cd page/academic_homepage
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
python build_static.py
```

这个脚本会自动执行以下操作：

* ✅ 安装所有依赖包
* ✅ 收集静态文件到 `staticfiles/`
* ✅ 生成中文版主页 (`docs/index.html`)
* ✅ 生成英文版主页 (`docs/index_en.html`)
* ✅ 生成所有专题页面 (讲座详情、项目页面、爱好页面等)
* ✅ 复制所有静态资源到 `docs/static/`
* ✅ 清理并重建 `docs/` 目录

生成完成后，`docs/` 目录将包含完整的静态网站文件。

## 🌐 部署到 GitHub Pages / Deploy to GitHub Pages

### 1. 推送代码到 GitHub / Push to GitHub

```bash
git add .
git commit -m "Update academic homepage"
git push origin main
```

### 2. 配置 GitHub Pages / Configure GitHub Pages

1. 进入 GitHub 仓库页面：[https://github.com/easygl1der/page](https://github.com/easygl1der/page)
2. 点击 **Settings** 标签页
3. 在左侧菜单中选择 **Pages**
4. 在 **Source** 部分：
   * 选择 **Deploy from a branch**
   * 选择 **main** 分支
   * 选择 **/ docs** 文件夹
5. 点击 **Save** 保存设置

### 3. 访问网站 / Access Website

几分钟后，网站将在以下地址可用：

```
https://easygl1der.github.io/page/
```

## 📁 项目结构 / Project Structure

```
page/
├── academic_homepage/             # 主项目目录
│   ├── academic_homepage/         # Django 项目配置
│   │   ├── settings.py           # 项目设置
│   │   ├── urls.py              # URL 配置
│   │   └── wsgi.py              # WSGI 配置
│   ├── homepage/                 # 主应用
│   │   ├── views.py             # 视图函数
│   │   ├── urls.py              # 应用 URL 配置
│   │   └── models.py            # 数据模型
│   ├── templates/                # Django 模板
│   │   ├── base.html            # 中文版基础模板
│   │   ├── base_en.html         # 英文版基础模板
│   │   ├── index.html           # 中文版主页模板
│   │   ├── index_en.html        # 英文版主页模板
│   │   └── ...                  # 其他页面模板
│   ├── static/                   # 静态文件源码
│   │   ├── css/style.css        # 主样式文件
│   │   ├── images/              # 图片文件
│   │   └── files/               # 文档文件 (简历等)
│   ├── docs/                     # 生成的静态网站 (GitHub Pages)
│   │   ├── index.html           # 中文版主页
│   │   ├── index_en.html        # 英文版主页
│   │   ├── static/              # 静态资源
│   │   └── ...                  # 其他生成的页面
│   ├── build_static.py          # 自动化构建脚本
│   ├── build_docs.py            # 备用构建脚本
│   ├── requirements.txt         # Python 依赖
│   ├── manage.py                # Django 管理命令
│   └── README.md                # 项目说明
```

## 🎨 自定义内容 / Customization

### 修改个人信息 / Update Personal Information

1. **基本信息**：编辑 `templates/index.html` 和 `templates/index_en.html`
2. **头像照片**：替换 `static/images/profile.jpg`
3. **简历文件**：替换 `static/files/resume_yueyihua.pdf`
4. **联系方式**：更新模板中的邮箱、GitHub、Telegram等链接
5. **主要样式**：修改 `static/css/style.css`

### 添加新页面 / Add New Pages

1. 在 `templates/` 中创建新模板
2. 在 `homepage/views.py` 中添加视图函数
3. 在 `homepage/urls.py` 中添加 URL 配置
4. 更新 `build_static.py` 脚本以生成新页面

### 修改主题 / Theme Customization

编辑模板文件中的 CSS 变量：

```css
:root {
    --text-primary: #1f2937;
    --text-secondary: #6b7280;
    --accent-color: #007bff;
    --card-bg: 255, 255, 255;
}

.dark-theme {
    --text-primary: #ffffff;
    --text-secondary: #d1d5db;
    --accent-color: #4dabf7;
    --card-bg: 42, 42, 62;
}
```

## 🔧 开发工具 / Development Tools

### 自动化脚本 / Automation Scripts

* `build_static.py` - 主要的静态网站生成脚本
* `build_docs.py` - 备用构建脚本
* `manage.py` - Django 管理命令

### 有用的命令 / Useful Commands

```bash
# 创建超级用户
python manage.py createsuperuser

# 运行测试
python manage.py test

# 检查项目
python manage.py check

# 收集静态文件
python manage.py collectstatic

# 生成静态网站
python build_static.py
```

## 📝 更新流程 / Update Workflow

1. **修改内容**：更新模板文件、静态资源或个人信息
2. **生成静态网站**：运行 `python build_static.py`
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
   * 确保运行了 `python manage.py collectstatic`
   * 检查 `STATIC_ROOT` 设置
   
2. **GitHub Pages 不更新**
   * 确保推送了 `docs/` 目录
   * 检查 GitHub Pages 设置是否正确
   * 查看 Actions 标签页的构建状态
   
3. **样式不生效**
   * 清除浏览器缓存
   * 检查 CSS 文件路径
   * 确认静态文件已正确收集

4. **中英文切换问题**
   * 检查 URL 配置
   * 确认模板文件存在

### 获取帮助 / Get Help

如果遇到问题，请：

1. 检查浏览器控制台错误信息
2. 查看 GitHub Pages 构建日志
3. 提交 Issue 到项目仓库

## 📄 许可证 / License

本项目采用 CC BY NC ND 4.0 许可协议。

## 🤝 贡献 / Contributing

欢迎提交 Pull Request 或 Issue！

## 📞 联系方式 / Contact

* **姓名** / Name: 乐绎华 / Yue Yihua
* **邮箱** / Email: yueyh@mail2.sysu.edu.cn
* **GitHub**: [https://github.com/easygl1der](https://github.com/easygl1der)
* **Telegram**: @LUCIFERASER
* **学术主页** / Homepage: [https://easygl1der.github.io/page/](https://easygl1der.github.io/page/)

---

⭐ 如果这个项目对你有帮助，请给它一个星标！

⭐ If this project helps you, please give it a star!

## 🎯 项目亮点 / Project Highlights

* ✨ **现代化UI设计** - 采用简约风格，支持白天/夜晚主题切换
* 🌍 **完整双语支持** - 中英文内容完全对应，URL路由分离
* 📱 **完美响应式** - 适配桌面端和移动端，导航栏自适应
* 🚀 **一键部署** - 自动化构建脚本，无需手动配置
* 🎨 **交互式元素** - 悬停动画、渐变效果、3D卡片样式
* 📧 **社交媒体集成** - 支持多种联系方式的快速访问 