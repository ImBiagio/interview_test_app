from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets, permissions

from .forms import CommentForm
from .models import Article, Comment
from .serializers import ArticleSerializer


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


# Detail view
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        article = self.get_object()
        comments = Comment.objects.filter(article=article)
        contex["comments"] = comments
        contex["form"] = CommentForm()
        return contex

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = self.object
            comment.author = self.request.user
            comment.save()
            return redirect("article_detail", pk=self.object.pk)
        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)


# Create view
class ArticleCreateView(CreateView, LoginRequiredMixin):
    model = Article
    template_name = 'blog/article_form.html'
    fields = ['title', 'content']

    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Update view
class ArticleUpdateView(UpdateView, LoginRequiredMixin):
    model = Article
    template_name = 'blog/article_form.html'
    fields = ['title', 'content']

    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.object.pk})


# Delete view
class ArticleDeleteView(DeleteView, LoginRequiredMixin):
    model = Article
    template_name = 'blog/article_delete.html'
    success_url = reverse_lazy('article_list')


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-published_date')
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
