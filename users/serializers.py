from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    username = serializers.CharField(
        max_length=50,
        validators=[
            UniqueValidator(User.objects.all(), message="username already taken.")
        ],
    )
    password = serializers.CharField(min_length=4, write_only=True)

    email = serializers.EmailField(
        max_length=127,
        validators=[
            UniqueValidator(User.objects.all(), message="email already registered.")
        ],
    )
    first_name = serializers.CharField(max_length=50)
    is_employee = serializers.BooleanField(default=False)

    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(allow_null=False, default=None)

    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict) -> User:
        if validated_data.get("is_employee"):
            return User.objects.create_superuser(**validated_data)
        else:
            return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:

        for key, value in validated_data.items():
            setattr(instance, key, value)

            if key == "password":
                instance.set_password(value)

        instance.save()

        return instance
