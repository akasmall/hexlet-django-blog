from django.views.generic import TemplateView


class IndexViewArticle(TemplateView):

    template_name = 'article/index.html'  # Указываем шаблон с полным путем

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # tags = self.kwargs.get('tags')
        # article_id = self.kwargs.get('article_id')
        tags = self.kwargs.get('tags', '')
        article_id = self.kwargs.get('article_id', None)

        if article_id is not None and tags != '':
            context['article_id'] = article_id
            context['tags'] = tags
        else:
            context['article'] = 'article'

        return context
