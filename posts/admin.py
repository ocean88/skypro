from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_link', 'created_at')
    list_filter = ('created_at',)  # Note the comma to make it a tuple

    def author_link(self, obj):
        return obj.author
    author_link.short_description = 'Автор'
    author_link.admin_order_field = 'author'  # Corrected 'Author' to 'author'

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'post', 'created_at')
    list_filter = ('created_at',)  # Note the comma to make it a tuple

admin.site.register(Comment, CommentAdmin)