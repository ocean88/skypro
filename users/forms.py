
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .validators import validate_password, validate_email_domain

class CustomUserCreationForm(UserCreationForm):
    # Поля формы для регистрации
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput,
        validators=[validate_password]
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput,
        validators=[validate_password]
    )
    email = forms.EmailField(
        label="Email",
        validators=[validate_email_domain]
    )
    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        validate_password(password1)
        return password1

    def clean_email(self):
        email = self.cleaned_data.get('email')
        validate_email_domain(email)
        return email
