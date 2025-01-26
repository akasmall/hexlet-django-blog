# hexlet_django_blog/article/views.py
from django.shortcuts import render


def index(request):
    return render(
        request,
        'article/index.html',
        context={'article': 'article'},
    )
