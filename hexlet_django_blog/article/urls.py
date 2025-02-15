from django.urls import path

from hexlet_django_blog.article.views import IndexViewArticle

urlpatterns = [
    path('', IndexViewArticle.as_view(), name='index'),
    path('<str:tags>/<int:article_id>/',
         IndexViewArticle.as_view(), name='article'),
]
