from django.urls import path

from .views import article_list, ArticleListView

urlpatterns = [
    path('list-fbv', article_list, name='article_list'),
    path('list-cbv', ArticleListView.as_view(), name='article_list'),

]