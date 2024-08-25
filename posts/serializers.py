from rest_framework import serializers
from .models import Post, Comment
from users.serializers import UserSerializer

class CommentModelSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'created_at', 'updated_at']

class PostModelSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentModelSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'image', 'author', 'comments', 'created_at', 'updated_at']