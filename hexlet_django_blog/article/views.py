from django.views.generic import TemplateView


class IndexViewArticle(TemplateView):

    template_name = 'article/index.html'  # Указываем шаблон с полным путем

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = 'article'
        return context
