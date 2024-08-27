from django.core.exceptions import ValidationError


# Валидатор для проверки запрещенных слов
def validate_title(value):
    forbidden_words = ['eрунда', 'глупость', 'чепуха']
    for word in forbidden_words:
        if word in value.lower():
            raise ValidationError(
                "Заголовок содержит бранные слова: %(words)s"
            )