from rest_framework import serializers
from users.models import User
from users.validators import validate_author_age, validate_email_domain, validate_password  


class UserSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = User
        fields = "__all__"

        def validate(self, data):
            user.instance = User(**data)

            validate_author_age(user.instance)
            validate_email_domain(user.instance)
            validate_password(user.instance)
            return data

