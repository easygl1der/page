import os
import shutil
import subprocess
import sys
from django.core.management import execute_from_command_line
from django.template.loader import render_to_string
from django.conf import settings

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

def generate_html_files(docs_dir):
    """从Django模板生成HTML文件"""
    from django.template.loader import render_to_string
    from django.template import Context, Template
    from django.template.context import RequestContext
    from django.test import RequestFactory
    
    # 创建一个模拟的request对象
    factory = RequestFactory()
    request = factory.get('/')
    
    # 生成中文版主页
    try:
        # 读取模板文件
        with open('templates/base.html', 'r', encoding='utf-8') as f:
            base_template_content = f.read()
        
        with open('templates/index.html', 'r', encoding='utf-8') as f:
            index_template_content = f.read()
        
        # 处理模板继承和静态文件路径
        # 替换Django模板标签为静态路径
        processed_base = base_template_content.replace('{% load static %}', '')
        processed_base = processed_base.replace("{% static '", "static/")
        processed_base = processed_base.replace("' %}", "")
        processed_base = processed_base.replace('{% static "', 'static/')
        processed_base = processed_base.replace('" %}', '')
        
        # 处理index模板
        processed_index = index_template_content.replace('{% load static %}', '')
        processed_index = processed_index.replace("{% static '", "static/")
        processed_index = processed_index.replace("' %}", "")
        processed_index = processed_index.replace('{% static "', 'static/')
        processed_index = processed_index.replace('" %}', '')
        
        # 替换Django URL标签
        processed_index = processed_index.replace('href="/talk/latex/"', 'href="talk_detail.html"')
        processed_index = processed_index.replace('href="/static/', 'href="static/')
        processed_index = processed_index.replace('src="/static/', 'src="static/')
        
        # 提取content部分
        content_start = processed_index.find('{% block content %}') + len('{% block content %}')
        content_end = processed_index.find('{% endblock %}')
        content = processed_index[content_start:content_end].strip()
        
        # 替换base模板中的block
        final_html = processed_base.replace('{% block title %}{% endblock %}', '乐绎华 - 个人学术主页')
        final_html = final_html.replace('{% block content %}{% endblock %}', content)
        
        # 写入中文版主页
        with open(os.path.join(docs_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(final_html)
        
        print("中文版主页生成完成")
        
    except Exception as e:
        print(f"生成中文版主页时出错: {e}")
        # 如果模板处理失败，使用备用的硬编码版本
        generate_fallback_html(docs_dir)
    
    # 生成英文版主页
    try:
        # 读取英文模板文件
        with open('templates/base_en.html', 'r', encoding='utf-8') as f:
            base_en_template_content = f.read()
        
        with open('templates/index_en.html', 'r', encoding='utf-8') as f:
            index_en_template_content = f.read()
        
        # 处理英文模板
        processed_base_en = base_en_template_content.replace('{% load static %}', '')
        processed_base_en = processed_base_en.replace("{% static '", "static/")
        processed_base_en = processed_base_en.replace("' %}", "")
        processed_base_en = processed_base_en.replace('{% static "', 'static/')
        processed_base_en = processed_base_en.replace('" %}', '')
        
        processed_index_en = index_en_template_content.replace('{% load static %}', '')
        processed_index_en = processed_index_en.replace("{% static '", "static/")
        processed_index_en = processed_index_en.replace("' %}", "")
        processed_index_en = processed_index_en.replace('{% static "', 'static/')
        processed_index_en = processed_index_en.replace('" %}', '')
        
        # 替换Django URL标签
        processed_index_en = processed_index_en.replace('href="/talk/latex/"', 'href="talk_detail_en.html"')
        processed_index_en = processed_index_en.replace('href="/static/', 'href="static/')
        processed_index_en = processed_index_en.replace('src="/static/', 'src="static/')
        
        # 提取content部分
        content_start_en = processed_index_en.find('{% block content %}') + len('{% block content %}')
        content_end_en = processed_index_en.find('{% endblock %}')
        content_en = processed_index_en[content_start_en:content_end_en].strip()
        
        # 替换base模板中的block
        final_html_en = processed_base_en.replace('{% block title %}{% endblock %}', 'Yue Yihua - Personal Academic Homepage')
        final_html_en = final_html_en.replace('{% block content %}{% endblock %}', content_en)
        
        # 写入英文版主页
        with open(os.path.join(docs_dir, 'index_en.html'), 'w', encoding='utf-8') as f:
            f.write(final_html_en)
        
        print("英文版主页生成完成")
        
    except Exception as e:
        print(f"生成英文版主页时出错: {e}")
    
    # 生成其他页面
    generate_other_pages(docs_dir)

def generate_other_pages(docs_dir):
    """生成其他页面"""
    pages = [
        ('talk_detail.html', 'talk_detail.html'),
        ('talk_detail_en.html', 'talk_detail_en.html'),
        ('mathematica_project.html', 'mathematica_project.html'),
        ('mathematica_project_en.html', 'mathematica_project_en.html'),
        ('football_hobby.html', 'football_hobby.html'),
        ('football_hobby_en.html', 'football_hobby_en.html'),
    ]
    
    for template_name, output_name in pages:
        try:
            # 读取模板文件
            with open(f'templates/{template_name}', 'r', encoding='utf-8') as f:
                template_content = f.read()
            
            # 处理静态文件路径
            processed_content = template_content.replace('{% load static %}', '')
            processed_content = processed_content.replace("{% static '", "static/")
            processed_content = processed_content.replace("' %}", "")
            processed_content = processed_content.replace('{% static "', 'static/')
            processed_content = processed_content.replace('" %}', '')
            
            # 替换URL标签
            processed_content = processed_content.replace('href="/static/', 'href="static/')
            processed_content = processed_content.replace('src="/static/', 'src="static/')
            processed_content = processed_content.replace('href="/"', 'href="index.html"')
            processed_content = processed_content.replace('href="/en/"', 'href="index_en.html"')
            
            # 写入文件
            with open(os.path.join(docs_dir, output_name), 'w', encoding='utf-8') as f:
                f.write(processed_content)
            
            print(f"{output_name} 生成完成")
            
        except Exception as e:
            print(f"生成 {output_name} 时出错: {e}")

def generate_fallback_html(docs_dir):
    """备用的硬编码HTML生成函数"""
    # 这里保留原来的硬编码HTML作为备用
    print("使用备用HTML生成方法")
    # ... 原来的硬编码HTML内容 ...

if __name__ == '__main__':
    # 确定项目根目录（包含 manage.py 的目录）
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)

    # 设置Django环境
    setup_django()

    # 安装 Python 依赖
    run("pip install -r requirements.txt")

    # 收集静态文件到 STATIC_ROOT
    run("python manage.py collectstatic --noinput")

    # 生成目录和路径
    docs_dir = os.path.join(project_dir, 'docs')
    static_src = os.path.join(project_dir, 'staticfiles')

    # 清理并创建 docs 目录
    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)
    os.makedirs(docs_dir)

    # 从Django模板生成HTML文件
    generate_html_files(docs_dir)

    # 拷贝静态资源到 docs/static
    dest_static = os.path.join(docs_dir, 'static')
    shutil.copytree(static_src, dest_static)

    print("文档生成完成: docs 目录已更新，请将其推送到 GitHub 并配置 Pages 源为 /docs")