from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, read_only=True)
    class Meta:
        model = Post
        fields = ["id", "title", "slug", "author"]