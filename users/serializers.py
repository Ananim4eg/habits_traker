from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import CustomUser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Сериализатор для токенов"""
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        return token


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации пользователя"""
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'telegram_id', 'password', 'confirm_password',)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Пароли должны совпадать!")
        if not data['telegram_id'].isdigit():
            raise serializers.ValidationError('Телеграм ID должен содержать только цифры')
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = CustomUser.objects.create_user(**validated_data)
        return user
