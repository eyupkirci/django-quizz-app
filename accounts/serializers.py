from rest_framework import serializers, validators

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=True)
    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(
        required=True,
        write_only=True,
        style={"type":"password"},
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        required=True,
        write_only=True,
        style={"input_type":"password"},
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2'
        ]
        extra_kwargs = {
            "password": {"write_only":True},
            "password2": {"write_only":True}
        }
    
    def create(self, data):
        password = data.get("password")
        data.pop("password2")

        user = User.objects.create(**data)
        user.password = make_password(password)
        user.save()
        return user

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data