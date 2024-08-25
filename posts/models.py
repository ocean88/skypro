from django.db import models
from users.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(User, through='Comment', related_name='post_comments', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'(self.title)'
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'(self.text)'
    
    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'