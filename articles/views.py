from django.views.generic import ListView, TemplateView, DetailView

from .models import Article, Excerpts


# Create your views here.

class AboutView(TemplateView):
    template_name = "articles/about.html"


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'articles/article_list.html'
    paginate_by = 2
    ordering = ['data']


class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/detail_article.html"


class ExcerptsListView(ListView):
    model = Excerpts
    context_object_name = 'excerpts'
    paginate_by = 3
    template_name = 'articles/excerpts_list.html'
