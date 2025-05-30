import os
import shutil
import subprocess
import sys
import re

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

def process_template_content(content):
    """处理模板内容，替换Django标签为静态路径"""
    # 移除load static标签
    content = re.sub(r'{%\s*load\s+static\s*%}', '', content)
    
    # 替换static标签
    content = re.sub(r'{%\s*static\s+[\'"]([^\'"]+)[\'"]\s*%}', r'static/\1', content)
    
    # 替换URL标签
    content = re.sub(r'{%\s*url\s+[\'"]talk_detail[\'"].*?%}', 'talk_detail.html', content)
    content = re.sub(r'{%\s*url\s+[\'"]talk_detail_en[\'"].*?%}', 'talk_detail_en.html', content)
    content = re.sub(r'{%\s*url\s+[\'"]mathematica_project[\'"].*?%}', 'mathematica_project.html', content)
    content = re.sub(r'{%\s*url\s+[\'"]mathematica_project_en[\'"].*?%}', 'mathematica_project_en.html', content)
    content = re.sub(r'{%\s*url\s+[\'"]football_hobby[\'"].*?%}', 'football_hobby.html', content)
    content = re.sub(r'{%\s*url\s+[\'"]football_hobby_en[\'"].*?%}', 'football_hobby_en.html', content)
    content = re.sub(r'{%\s*url\s+[\'"]home[\'"].*?%}', 'index.html', content)
    content = re.sub(r'{%\s*url\s+[\'"]home_en[\'"].*?%}', 'index_en.html', content)
    content = re.sub(r'{%\s*url\s+[\'"]home_cn[\'"].*?%}', 'index.html', content)
    
    # 替换直接的URL路径
    content = content.replace('href="/talk/latex/"', 'href="talk_detail.html"')
    content = content.replace('href="/talk/latex_en/"', 'href="talk_detail_en.html"')
    content = content.replace('href="/project/mathematica/"', 'href="mathematica_project.html"')
    content = content.replace('href="/project/mathematica_en/"', 'href="mathematica_project_en.html"')
    content = content.replace('href="/hobby/football/"', 'href="football_hobby.html"')
    content = content.replace('href="/hobby/football_en/"', 'href="football_hobby_en.html"')
    content = content.replace('href="/"', 'href="index.html"')
    content = content.replace('href="/en/"', 'href="index_en.html"')
    content = content.replace('href="/cn/"', 'href="index.html"')
    
    # 替换JavaScript中的语言切换链接
    content = content.replace("window.location.href = '/en/';", "window.location.href = 'index_en.html';")
    content = content.replace("window.location.href = '/cn/';", "window.location.href = 'index.html';")
    
    # 确保静态文件路径正确
    content = content.replace('href="/static/', 'href="static/')
    content = content.replace('src="/static/', 'src="static/')
    
    return content

def merge_templates(base_template, content_template, title):
    """合并base模板和内容模板"""
    # 处理内容模板
    content_processed = process_template_content(content_template)
    
    # 提取content block
    content_match = re.search(r'{%\s*block\s+content\s*%}(.*?){%\s*endblock\s*%}', content_processed, re.DOTALL)
    if content_match:
        content_block = content_match.group(1).strip()
    else:
        # 如果没有找到block标签，尝试提取extends之后的所有内容
        extends_match = re.search(r'{%\s*extends.*?%}', content_processed)
        if extends_match:
            content_block = content_processed[extends_match.end():].strip()
        else:
            content_block = content_processed
    
    # 处理base模板，但保留block标签
    base_content = base_template
    # 只处理static标签，保留block标签
    base_content = re.sub(r'{%\s*load\s+static\s*%}', '', base_content)
    base_content = re.sub(r'{%\s*static\s+[\'"]([^\'"]+)[\'"]\s*%}', r'static/\1', base_content)
    base_content = base_content.replace('href="/static/', 'href="static/')
    base_content = base_content.replace('src="/static/', 'src="static/')
    
    # 替换base模板中的blocks
    final_html = base_content.replace('{% block title %}{% endblock %}', title)
    
    # 使用正则表达式替换content block，处理可能的空白字符
    content_block_pattern = r'{%\s*block\s+content\s*%}\s*{%\s*endblock\s*%}'
    final_html = re.sub(content_block_pattern, content_block, final_html)
    
    # 最后清理剩余的Django标签
    final_html = re.sub(r'{%.*?%}', '', final_html)
    final_html = re.sub(r'{{.*?}}', '', final_html)
    
    return final_html

def generate_html_files(docs_dir):
    """从Django模板生成HTML文件"""
    
    # 页面配置
    pages = [
        {
            'base': 'templates/base.html',
            'content': 'templates/index.html',
            'output': 'index.html',
            'title': '乐绎华 - 个人学术主页'
        },
        {
            'base': 'templates/base_en.html',
            'content': 'templates/index_en.html',
            'output': 'index_en.html',
            'title': 'Yue Yihua - Personal Academic Homepage'
        }
    ]
    
    # 生成主页
    for page in pages:
        try:
            # 读取模板文件
            with open(page['base'], 'r', encoding='utf-8') as f:
                base_template = f.read()
            
            with open(page['content'], 'r', encoding='utf-8') as f:
                content_template = f.read()
            
            # 合并模板
            final_html = merge_templates(base_template, content_template, page['title'])
            
            # 写入文件
            with open(os.path.join(docs_dir, page['output']), 'w', encoding='utf-8') as f:
                f.write(final_html)
            
            print(f"{page['output']} 生成完成")
            
        except Exception as e:
            print(f"生成 {page['output']} 时出错: {e}")
    
    # 生成其他页面（这些页面已经是完整的HTML）
    other_pages = [
        'talk_detail.html',
        'talk_detail_en.html',
        'mathematica_project.html',
        'mathematica_project_en.html',
        'football_hobby.html',
        'football_hobby_en.html',
    ]
    
    for page_name in other_pages:
        try:
            # 读取模板文件
            with open(f'templates/{page_name}', 'r', encoding='utf-8') as f:
                template_content = f.read()
            
            # 处理模板内容
            processed_content = process_template_content(template_content)
            
            # 清理Django标签
            processed_content = re.sub(r'{%.*?%}', '', processed_content)
            processed_content = re.sub(r'{{.*?}}', '', processed_content)
            
            # 写入文件
            with open(os.path.join(docs_dir, page_name), 'w', encoding='utf-8') as f:
                f.write(processed_content)
            
            print(f"{page_name} 生成完成")
            
        except Exception as e:
            print(f"生成 {page_name} 时出错: {e}")

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