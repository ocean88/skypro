from django.core.exceptions import ValidationError
from datetime import date

# проверка пароля
def validate_password(value):
    if len(value) < 8:
        raise ValidationError(
            'должен быть не менее 8 символов, должен включать цифры'
        )
    if not any(char.isdigit() for char in value):
        raise ValidationError(
            'Пароль должен содержать хотя бы одну цифру'
        )
    

# проверка для почты

def validate_email_domain(value):
    allowed_domains = ["mail.ru", "yandex.ru"]
    domain = value.split("@")[-1]
    if domain not in allowed_domains:
        raise ValidationError(
            f'Разрешены только следующие домены для регистрации: {allowed_domains}'
        )
    

def validate_author_age(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 18:
        raise ValidationError("Автор должен быть старше 18 лет, чтобы публиковать посты")