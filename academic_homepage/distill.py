from django.urls import reverse

def get_distill_urls():
    return [
        (reverse('index'), 'index.html'),
        (reverse('talk_detail'), 'talk_detail.html'),
        (reverse('mathematica_project'), 'mathematica_project.html'),
        (reverse('football_hobby'), 'football_hobby.html'),
        (reverse('index_en'), 'index_en.html'),
        (reverse('talk_detail_en'), 'talk_detail_en.html'),
        (reverse('mathematica_project_en'), 'mathematica_project_en.html'),
        (reverse('football_hobby_en'), 'football_hobby_en.html'),
    ] 