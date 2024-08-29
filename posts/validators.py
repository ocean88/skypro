from rest_framework.exceptions import ValidationError
from datetime import date

def validate_author_age(author):
    if not author.date_of_birth:
        raise ValidationError("Дата рождения не указана")
    
    today = date.today()
    age = today.year - author.date_of_birth.year - ((today.month, today.day) < (author.date_of_birth.month, author.date_of_birth.day))
    
    if age < 18:
        raise ValidationError("Автор должен быть старше 18 лет")