from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'published_date', 'author']
        read_only_fields = ['id', 'published_date', 'author']
