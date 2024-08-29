from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostModelSerializer, CommentModelSerializer
from .permissions import IsOwnerOrAdmin, IsAuthenticatedOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.context['author'] = self.request.user  # Добавляем авторизованного пользователя в контекст сериализатора
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
