from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post

class AuthorSeializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username','email']


class PostSerializer(serializers.ModelSerializer):
    # username = serializers.ReadOnlyField(source='author.username')
    author = AuthorSeializer()
    class Meta:
        model = Post
        fields = [
            'pk',
            'author',
            'message',
            'created_at',
            'updated_at',
            'is_public',
        ]