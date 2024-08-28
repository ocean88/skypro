from django.shortcuts import render
from users.models import User
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from users.serializers import UserSerializer
from rest_framework.permissions import AllowAny
from .permissions import IsAdminOrSelf


class UserCreateAPIView(CreateAPIView):
    """Создание пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    """Просмотр, редактирование и удаление пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminOrSelf]