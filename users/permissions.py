from rest_framework.permissions import BasePermission


class IsAdminOrSelf(BasePermission):
    """
    Разрешает редактировать или удалять только свой профиль или если пользователь администратор.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user
