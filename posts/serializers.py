from rest_framework import serializers
from .models import Post, Comment
from users.serializers import UserSerializer
from rest_framework.serializers import ValidationError
from datetime import date


class PostModelSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"

    def validate_title(self, value):
        forbidden_words = ['ерунда', 'глупость', 'чепуха']
        for word in forbidden_words:
            if word in value.lower():
                raise ValidationError(
                    f"Заголовок содержит бранные слова: {word}"
                )
        return value


    def validate(self, data):
        author = data.get('author')
        if author and author.date_of_birth:
            age = timezone.now().date().year - author.date_of_birth.year
            if timezone.now().date() < author.date_of_birth.replace(year=timezone.now().date().year):
                age -= 1
            if age < 18:
                raise serializers.ValidationError("Автор поста должен быть старше 18 лет.")
        return data


class CommentModelSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
