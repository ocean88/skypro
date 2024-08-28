from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Разрешает доступ на чтение всем, но доступ на запись только администраторам.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff


class IsOwnerOrAdminOrReadOnly(BasePermission):
    """
    Разрешает редактировать или удалять объекты только их владельцам или администраторам.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user or request.user.is_staff


class IsOwnerOrAdmin(BasePermission):
    """
    Разрешает редактировать или удалять объекты только их владельцам или администраторам.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.author == request.user


class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated
