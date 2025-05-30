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
    """手动生成HTML文件"""
    from django.template.loader import get_template
    from django.template import Context
    
    # 生成中文版主页
    index_content = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>乐绎华 - 个人学术主页</title>
    <link rel="stylesheet" href="static/css/style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="icon" type="image/x-icon" href="static/images/favicon.ico">
</head>
<body class="light-theme">
    <header>
        <nav class="navbar">
            <div class="nav-brand">
                <a href="index.html" class="brand-link">乐绎华</a>
            </div>
            <div class="nav-menu">
                <a href="#bio" class="nav-link">关于我</a>
                <a href="#talks" class="nav-link">讲座</a>
                <a href="#projects" class="nav-link">项目</a>
                <a href="#awards" class="nav-link">获奖</a>
                <a href="#hobbies" class="nav-link">爱好</a>
                <a href="index_en.html" class="nav-link lang-switch">English</a>
            </div>
            <div class="theme-controls">
                <button id="theme-toggle" class="theme-btn" title="切换主题">
                    <i class="fas fa-sun"></i>
                </button>
            </div>
        </nav>
    </header>

    <main>
        <section id="bio" class="hero">
            <div class="hero-content">
                <div class="profile">
                    <h1>👋 你好，我是乐绎华</h1>
                    <h2>数学本科生，中山大学</h2>
                    <p>我是一名对数学充满热情的本科生，即将进入大三。我特别热衷于探索偏微分方程、高等概率论和代数几何等领域。</p>
                    <div class="interests">
                        <h3>研究兴趣</h3>
                        <ul>
                            <li>偏微分方程 (Partial Differential Equations)</li>
                            <li>概率论 (Probability Theory)</li>
                            <li>代数几何 (Algebraic Geometry)</li>
                        </ul>
                    </div>
                    <div class="education">
                        <h3>教育背景</h3>
                        <ul>
                            <li><strong>数学学士</strong> - 中山大学 (2023年9月至今)</li>
                        </ul>
                    </div>
                </div>
                <div class="profile-photo">
                    <img src="static/images/profile.jpg" alt="乐绎华的照片" class="tilted-photo">
                    
                    <!-- Contact Icons under photo -->
                    <div class="bio-contact-icons">
                        <a href="static/files/resume_yueyihua.pdf" target="_blank" class="bio-icon resume" title="下载简历">
                            <i class="fas fa-file-pdf"></i>
                        </a>
                        <a href="mailto:yueyh@mail2.sysu.edu.cn" class="bio-icon email" title="发送邮件">
                            <svg class="heroicon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207"/>
                            </svg>
                        </a>
                        <a href="https://github.com/easygl1der" target="_blank" class="bio-icon github" title="GitHub">
                            <i class="fab fa-github"></i>
                        </a>
                        <a href="talk_detail.html" class="bio-icon talk" title="讲座">
                            <i class="fas fa-chalkboard-teacher"></i>
                        </a>
                    </div>
                </div>
            </div>
        </section>

        <section id="talks">
            <h2>🎤 讲座与分享</h2>
            <div class="talks-list">
                <a href="talk_detail.html" class="talk-item-link">
                    <div class="talk-item clickable-talk">
                        <div class="talk-header">
                            <h3>LaTeX 高级入门讲座</h3>
                            <div class="talk-image">
                                <img src="static/images/latex-talk-2.jpg" alt="LaTeX讲座现场" class="talk-photo">
                            </div>
                        </div>
                        <div class="talk-content">
                            <div class="talk-meta">
                                <div class="talk-time">
                                    <i class="fas fa-calendar-alt"></i>
                                    <span>2024年11月15日 19:00-22:00</span>
                                </div>
                                <div class="talk-location">
                                    <i class="fas fa-map-marker-alt"></i>
                                    <span>392栋301黄传经堂</span>
                                </div>
                            </div>
                            <div class="talk-description">
                                <p>为新生介绍LaTeX的基础知识，如LaTeX的基础功能，安装方法，使用技巧等等。本活动由SPS物理协会与笃行工作室联合举办。</p>
                            </div>
                        </div>
                        <div class="talk-action">
                            <span class="talk-link-text">点击查看详情 →</span>
                        </div>
                    </div>
                </a>
            </div>
        </section>

        <section id="projects">
            <h2>📑 我的Mathematica项目</h2>
            <div class="projects-list">
                <a href="mathematica_project.html" class="project-item-link">
                    <div class="project-item clickable-project">
                        <h3>Lane-Emden-Fowler方程的数值求解研究</h3>
                        <p><strong>摘要：</strong>Lane-Emden-Fowler方程是一类二阶非线性微分方程，在天体力学、流体力学、热力学等领域有着广泛应用，可用来描述恒星结构、热传导等现象。</p>
                        <p><strong>关键词：</strong>Mathematica, Lane-Emden-Fowler方程, 数值分析, LH-HPM, 分数阶导数</p>
                        <div class="project-action">
                            <span class="project-link-text">点击查看详情 →</span>
                        </div>
                    </div>
                </a>
            </div>
        </section>

        <section id="awards">
            <h2>🏆 获奖经历</h2>
            <div class="awards-list">
                <a href="https://mp.weixin.qq.com/s/aZOxVwuB1lkwG64KBbxHVA" target="_blank" class="award-item-link">
                    <div class="award-item clickable-award">
                        <h3>国家奖学金</h3>
                        <p>2023-2024学年 国家级奖学金</p>
                        <div class="award-action">
                            <span class="award-link-text">查看信息 →</span>
                        </div>
                    </div>
                </a>
                <div class="award-item clickable-award">
                    <h3>中山大学一等奖学金</h3>
                    <p>2023-2024学年 中山大学</p>
                </div>
                <a href="http://yau-contest.com/uploads/202505/27/1748321560229592.pdf" target="_blank" class="award-item-link">
                    <div class="award-item clickable-award">
                        <h3>2025年丘成桐大学生数学竞赛 - 分析与微分方程赛道优胜奖</h3>
                        <p>丘成桐大学生数学竞赛</p>
                        <div class="award-action">
                            <span class="award-link-text">查看信息 →</span>
                        </div>
                    </div>
                </a>
                <a href="http://yau-contest.com/uploads/202505/27/1748321521986447.pdf" target="_blank" class="award-item-link">
                    <div class="award-item clickable-award">
                        <h3>2025年丘成桐大学生数学竞赛 - 概率与统计赛道入围决赛</h3>
                        <p>丘成桐大学生数学竞赛</p>
                        <div class="award-action">
                            <span class="award-link-text">查看信息 →</span>
                        </div>
                    </div>
                </a>
                <a href="https://mp.weixin.qq.com/s/pLsQK1NePCJEvThrzODyEA" target="_blank" class="award-item-link">
                    <div class="award-item clickable-award">
                        <h3>第十五届全国大学生数学竞赛决赛（低年级组）一等奖</h3>
                        <p>全国排名第8名</p>
                        <div class="award-action">
                            <span class="award-link-text">查看信息 →</span>
                        </div>
                    </div>
                </a>
                <a href="https://mp.weixin.qq.com/s/Ub4s1H-VSKTMjKb46uZ1DQ" target="_blank" class="award-item-link">
                    <div class="award-item clickable-award">
                        <h3>第十六届全国大学生数学竞赛决赛（高年级组）一等奖</h3>
                        <p>中国数学会</p>
                        <div class="award-action">
                            <span class="award-link-text">查看信息 →</span>
                        </div>
                    </div>
                </a>
            </div>
        </section>

        <section id="hobbies">
            <h2>⚽ 我的爱好</h2>
            <div class="hobbies-list">
                <a href="football_hobby.html" class="hobby-item-link">
                    <div class="hobby-item clickable-hobby">
                        <h3>足球</h3>
                        <p>我热爱足球运动，经常参加校内足球比赛和友谊赛。足球不仅锻炼了我的身体，也培养了我的团队合作精神。</p>
                        <div class="hobby-action">
                            <span class="hobby-link-text">了解更多 →</span>
                        </div>
                    </div>
                </a>
            </div>
        </section>
    </main>

    <footer>
        <div class="footer-content">
            <p>&copy; 2024 乐绎华. 保留所有权利.</p>
            <div class="footer-links">
                <a href="mailto:yueyh@mail2.sysu.edu.cn">联系我</a>
                <a href="https://github.com/easygl1der" target="_blank">GitHub</a>
                <a href="static/files/resume_yueyihua.pdf" target="_blank">简历</a>
            </div>
        </div>
    </footer>

    <script>
        // Theme toggle functionality
        const themeToggle = document.getElementById('theme-toggle');
        const body = document.body;
        const themeIcon = themeToggle.querySelector('i');

        // Load saved theme
        const savedTheme = localStorage.getItem('theme') || 'light-theme';
        body.className = savedTheme;
        updateThemeIcon(savedTheme);

        themeToggle.addEventListener('click', () => {
            if (body.classList.contains('light-theme')) {
                body.className = 'dark-theme';
                localStorage.setItem('theme', 'dark-theme');
                updateThemeIcon('dark-theme');
            } else {
                body.className = 'light-theme';
                localStorage.setItem('theme', 'light-theme');
                updateThemeIcon('light-theme');
            }
        });

        function updateThemeIcon(theme) {
            if (theme === 'dark-theme') {
                themeIcon.className = 'fas fa-moon';
            } else {
                themeIcon.className = 'fas fa-sun';
            }
        }

        // Smooth scrolling for navigation links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    </script>
</body>
</html>'''
    
    # 写入中文版主页
    with open(os.path.join(docs_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print("HTML文件生成完成")

if __name__ == '__main__':
    # 确定项目根目录（包含 manage.py 的目录）
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)

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

    # 手动生成HTML文件
    generate_html_files(docs_dir)

    # 拷贝静态资源到 docs/static
    dest_static = os.path.join(docs_dir, 'static')
    shutil.copytree(static_src, dest_static)

    print("文档生成完成: docs 目录已更新，请将其推送到 GitHub 并配置 Pages 源为 /docs") 