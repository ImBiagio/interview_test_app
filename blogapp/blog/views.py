from django.shortcuts import render
from django.views.generic import ListView

from .models import Article


# Qui ho scritto 2 diverse view che fanno la stessa cosa, la prima è una function based view (FBV) e la seconda è una class based view (CBV).
# Class Based View (FBV)
class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
    ordering = ['-published_date']


# Function Based View (CBV)
def article_list(request):
    articles = Article.objects.all().order_by('-published_date')
    return render(request, 'blog/article_list.html', {'articles': articles})
