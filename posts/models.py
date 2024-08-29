from django.db import models
from django.conf import settings
from datetime import date
from django.utils import timezone
from rest_framework.serializers import ValidationError


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Comment', related_name='commented_posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()
        if self.author.date_of_birth:
            age = timezone.now().date().year - self.author.date_of_birth.year
            if timezone.now().date() < self.author.date_of_birth.replace(year=timezone.now().date().year):
                age -= 1
            if age < 18:
                raise ValidationError("Автор поста должен быть старше 18 лет.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Это вызовет метод clean() перед сохранением
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'



class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment_authors')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:50]  # Краткое представление текста комментария

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'