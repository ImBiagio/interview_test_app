from django.shortcuts import render

from .models import Article


def article_list(request):
    articles = Article.objects.all().order_by('-published_date')
    return render(request, 'blog/article_list.html', {'articles': articles})
