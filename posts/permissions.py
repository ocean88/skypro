from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Разрешение для проверки, является ли пользователь владельцем объекта или администратором.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешение на чтение - для всех
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешение на запись - только для владельца объекта или администратора
        return obj.author == request.user or request.user.is_staff


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Разрешение на создание только для авторизованных пользователей, чтение для всех.
    """

    def has_permission(self, request, view):
        # Разрешение на чтение - для всех
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешение на запись - только для авторизованных пользователей
        return request.user and request.user.is_authenticated
