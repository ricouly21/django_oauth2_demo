from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField("get_user")

    @staticmethod
    def get_user(instance):
        serializer = UserSerializer(instance.user)
        return serializer.data

    class Meta:
        model = Account
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'date_joined',
        ]
