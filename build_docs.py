import os
import shutil
import subprocess
import sys
import re
from datetime import datetime

def run(cmd, cwd=None):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd)
    if result.returncode != 0:
        print(f"Command failed: {cmd}", file=sys.stderr)
        sys.exit(result.returncode)

def setup_django():
    """设置Django环境"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'academic_homepage.settings')
    import django
    django.setup()

def process_django_template(template_content, is_base=False, page_title=""):
    """处理Django模板，转换为静态HTML"""
    # 移除{% load static %}标签
    content = re.sub(r'{% load static %}', '', template_content)
    
    # 处理{% static %}标签
    content = re.sub(r"{% static ['\"]([^'\"]+)['\"] %}", r'static/\1', content)
    
    # 处理{% url %}标签
    url_mappings = {
        'talk_detail': 'talk_detail.html',
        '/talk/latex/': 'talk_detail.html',
        '/project/mathematica/': 'mathematica_project.html',
        '/hobby/football/': 'football_hobby.html',
        '/cn/': 'index.html',
        '/en/': 'index_en.html',
        '/': 'index.html'
    }
    
    for url_name, static_url in url_mappings.items():
        content = re.sub(r"{% url ['\"]?" + re.escape(url_name) + r"['\"]? %}", static_url, content)
        content = content.replace(f'href="{url_name}"', f'href="{static_url}"')
    
    # 处理JavaScript中的语言切换URL - 修复GitHub Pages上的路径问题
    content = content.replace("window.location.href = '/cn/';", "window.location.href = 'index.html';")
    content = content.replace("window.location.href = '/en/';", "window.location.href = 'index_en.html';")
    
    # 处理导航菜单中的语言切换链接
    content = content.replace('href="/cn/"', 'href="index.html"')
    content = content.replace('href="/en/"', 'href="index_en.html"')
    
    # 处理{% now %}标签
    current_year = datetime.now().year
    content = re.sub(r'{% now ["\']Y["\'] %}', str(current_year), content)
    
    # 处理相对路径
    content = content.replace('href="/static/', 'href="static/')
    content = content.replace('src="/static/', 'src="static/')
    
    # 处理block标签（对于base模板）
    if is_base and page_title:
        # 替换title中的block标签
        content = re.sub(r'<title>{% block title %}.*?{% endblock %}</title>', f'<title>{page_title}</title>', content)
        # 替换其他地方的title block
        content = re.sub(r'{% block title %}.*?{% endblock %}', page_title, content)
    
    # 如果不是base模板，处理block标签
    if not is_base:
        # 移除extends标签
        content = re.sub(r'{% extends [^%]*%}', '', content)
        
        # 提取并返回content block的内容
        block_match = re.search(r'{% block content %}(.*?){% endblock %}', content, re.DOTALL)
        if block_match:
            block_content = block_match.group(1).strip()
            # 再次处理提取出的内容中的Django标签
            block_content = re.sub(r'{% load static %}', '', block_content)
            block_content = re.sub(r"{% static ['\"]([^'\"]+)['\"] %}", r'static/\1', block_content)
            # 处理{% url %}标签
            for url_name, static_url in url_mappings.items():
                block_content = re.sub(r"{% url ['\"]?" + re.escape(url_name) + r"['\"]? %}", static_url, block_content)
                block_content = block_content.replace(f'href="{url_name}"', f'href="{static_url}"')
            # 处理相对路径
            block_content = block_content.replace('href="/static/', 'href="static/')
            block_content = block_content.replace('src="/static/', 'src="static/')
            return block_content
    
    return content

def generate_page_from_templates(base_template_path, content_template_path, output_path, page_title):
    """从基础模板和内容模板生成完整页面"""
    try:
        # 读取基础模板
        with open(base_template_path, 'r', encoding='utf-8') as f:
            base_content = f.read()
        
        # 读取内容模板
        with open(content_template_path, 'r', encoding='utf-8') as f:
            content_template = f.read()
        
        # 处理基础模板，传递page_title
        processed_base = process_django_template(base_content, is_base=True, page_title=page_title)
        
        # 处理内容模板并提取content
        page_content = process_django_template(content_template, is_base=False)
        
        # 替换content
        final_html = processed_base.replace('{% block content %}{% endblock %}', page_content)
        
        # 写入文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_html)
        
        print(f"生成完成: {os.path.basename(output_path)}")
        return True
        
    except Exception as e:
        print(f"生成 {os.path.basename(output_path)} 时出错: {e}")
        return False

def generate_standalone_page(template_path, output_path):
    """生成独立页面（不继承base模板的页面）"""
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()
        
        # 处理模板
        processed_content = process_django_template(template_content, is_base=True)
        
        # 写入文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(processed_content)
        
        print(f"生成完成: {os.path.basename(output_path)}")
        return True
        
    except Exception as e:
        print(f"生成 {os.path.basename(output_path)} 时出错: {e}")
        return False

def generate_html_files(docs_dir):
    """从Django模板生成HTML文件"""
    templates_dir = 'templates'
    
    # 生成主要页面（使用模板继承）
    pages = [
        # (base_template, content_template, output_file, page_title)
        ('base.html', 'index.html', 'index.html', '乐绎华 - 个人学术主页'),
        ('base_en.html', 'index_en.html', 'index_en.html', 'Yue Yihua - Personal Academic Homepage'),
    ]
    
    for base_template, content_template, output_file, page_title in pages:
        base_path = os.path.join(templates_dir, base_template)
        content_path = os.path.join(templates_dir, content_template)
        output_path = os.path.join(docs_dir, output_file)
        
        generate_page_from_templates(base_path, content_path, output_path, page_title)
    
    # 生成独立页面（不继承base模板）
    standalone_pages = [
        ('talk_detail.html', 'talk_detail.html'),
        ('talk_detail_en.html', 'talk_detail_en.html'),
        ('mathematica_project.html', 'mathematica_project.html'),
        ('mathematica_project_en.html', 'mathematica_project_en.html'),
        ('football_hobby.html', 'football_hobby.html'),
        ('football_hobby_en.html', 'football_hobby_en.html'),
    ]
    
    for template_file, output_file in standalone_pages:
        template_path = os.path.join(templates_dir, template_file)
        output_path = os.path.join(docs_dir, output_file)
        
        if os.path.exists(template_path):
            generate_standalone_page(template_path, output_path)
        else:
            print(f"模板文件不存在: {template_path}")

def create_redirect_pages(docs_dir):
    """创建重定向页面以支持URL结构"""
    # 创建目录结构以支持Django URL模式
    subdirs = ['cn', 'en', 'talk', 'project', 'hobby']
    for subdir in subdirs:
        subdir_path = os.path.join(docs_dir, subdir)
        os.makedirs(subdir_path, exist_ok=True)
    
    # 创建重定向页面
    redirects = [
        ('cn/index.html', '../index.html'),
        ('en/index.html', '../index_en.html'),
        ('talk/latex/index.html', '../../talk_detail.html'),
        ('project/mathematica/index.html', '../../mathematica_project.html'),
        ('hobby/football/index.html', '../../football_hobby.html'),
    ]
    
    for redirect_file, target_url in redirects:
        redirect_path = os.path.join(docs_dir, redirect_file)
        os.makedirs(os.path.dirname(redirect_path), exist_ok=True)
        
        redirect_html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0;url={target_url}">
    <title>重定向中...</title>
</head>
<body>
    <p>正在重定向到 <a href="{target_url}">{target_url}</a></p>
</body>
</html>'''
        
        with open(redirect_path, 'w', encoding='utf-8') as f:
            f.write(redirect_html)
    
    print("重定向页面创建完成")

if __name__ == '__main__':
    # 确定项目根目录
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)

    # 设置Django环境
    setup_django()

    # 安装Python依赖
    run("pip install -r requirements.txt")

    # 收集静态文件
    run("python manage.py collectstatic --noinput")

    # 生成目录和路径
    docs_dir = os.path.join(project_dir, 'docs')
    static_src = os.path.join(project_dir, 'staticfiles')

    # 清理并创建docs目录
    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)
    os.makedirs(docs_dir)

    # 从Django模板生成HTML文件
    generate_html_files(docs_dir)

    # 创建重定向页面
    create_redirect_pages(docs_dir)

    # 拷贝静态资源到docs/static
    dest_static = os.path.join(docs_dir, 'static')
    shutil.copytree(static_src, dest_static)

    print("文档生成完成！")
    print("现在 docs/ 目录中的静态网站应该与本地 Django 网站保持一致。")
    print("请将更改推送到 GitHub 以更新静态网站。")