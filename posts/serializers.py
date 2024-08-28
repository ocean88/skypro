from rest_framework import serializers
from .models import Post, Comment
from users.serializers import UserSerializer
from posts.validators import validate_title


class CommentModelSerializer(serializers.ModelSerializer):


    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'created_at', 'updated_at']

    

class PostModelSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'image', 'author', 'comments', 'created_at', 'updated_at']

    def validate(self, data):
        posts.instance = Post(**data)

        validate_title(post.instance)
        return data
