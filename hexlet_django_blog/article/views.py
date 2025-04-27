from django.shortcuts import render
from django.views import View

from hexlet_django_blog.article.models import Article


class IndexViewArticle(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "article/index.html",
            context={
                "articles": articles,
            },
        )


# from django.views.generic import TemplateView


# class IndexViewArticle(TemplateView):

#     template_name = 'article/index.html'  # Указываем шаблон с полным путем

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         # tags = self.kwargs.get('tags')
#         # article_id = self.kwargs.get('article_id')
#         tags = self.kwargs.get('tags', '')
#         article_id = self.kwargs.get('article_id', None)

#         if article_id is not None and tags != '':
#             context['article_id'] = article_id
#             context['tags'] = tags
#         else:
#             context['article'] = 'article'

#         return context
