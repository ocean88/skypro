from rest_framework import serializers
from users.models import User
from django.contrib.auth import get_user_model
from users.validators import validate_author_age, validate_email_domain, validate_password  


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    email = serializers.EmailField(
        required=True,
        validators=[validate_email_domain]
    )

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Пароли не совпадают.")
        return data

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password1'])  # Устанавливаем пароль
        user.save()
        return user

