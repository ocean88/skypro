from django.contrib.auth.models import AbstractUser
from django.db import models
from users.validators import validate_email_domain, validate_password


# Модель User авторизация через Email
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email", validators=[validate_email_domain])
    password = models.CharField(max_length=128, validators=[validate_password])
    number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email