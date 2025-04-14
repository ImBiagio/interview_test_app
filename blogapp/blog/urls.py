from django.urls import path, include

from .views import article_list, ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, \
    ArticleDeleteView

urlpatterns = [
    path('list-fbv', article_list, name='article_list_fbv'),
    path('list-cbv', ArticleListView.as_view(), name='article_list'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
    path('api/', include('blog.api_urls')),

]
