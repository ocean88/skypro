# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import User

# Создание кастомной формы для редактирования пользователя в админке
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm

    # Поля, отображаемые в форме редактирования
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('number', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    # Поля, отображаемые в списке пользователей
    list_display = ('email', 'number', 'date_of_birth', 'is_staff')
    search_fields = ('email', 'number')
    ordering = ('email',)

# Регистрируем модель User с настройками CustomUserAdmin
admin.site.register(User, CustomUserAdmin)
