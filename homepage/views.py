from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def talk_detail(request):
    return render(request, 'talk_detail.html')

def mathematica_project(request):
    return render(request, 'mathematica_project.html')

def football_hobby(request):
    return render(request, 'football_hobby.html')

# English versions
def home_en(request):
    return render(request, 'home_en.html')

def index_en(request):
    return render(request, 'index_en.html')

def talk_detail_en(request):
    return render(request, 'talk_detail_en.html')

def mathematica_project_en(request):
    return render(request, 'mathematica_project_en.html')

def football_hobby_en(request):
    return render(request, 'football_hobby_en.html')
