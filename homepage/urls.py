from django.urls import path
from . import views

urlpatterns = [
    # Chinese version (default)
    path('', views.index, name='index'),
    path('about/', views.index, name='index'),
    path('talk/latex/', views.talk_detail, name='talk_detail'),
    path('project/mathematica/', views.mathematica_project, name='mathematica_project'),
    path('hobby/football/', views.football_hobby, name='football_hobby'),
    
    # Chinese version with explicit cn prefix
    path('cn/', views.index, name='index_cn'),
    path('cn/about/', views.index, name='index_cn'),
    path('cn/talk/latex/', views.talk_detail, name='talk_detail_cn'),
    path('cn/project/mathematica/', views.mathematica_project, name='mathematica_project_cn'),
    path('cn/hobby/football/', views.football_hobby, name='football_hobby_cn'),
    
    # English version
    path('en/', views.index_en, name='index_en'),
    path('en/about/', views.index_en, name='index_en'),
    path('en/talk/latex/', views.talk_detail_en, name='talk_detail_en'),
    path('en/project/mathematica/', views.mathematica_project_en, name='mathematica_project_en'),
    path('en/hobby/football/', views.football_hobby_en, name='football_hobby_en'),
] 