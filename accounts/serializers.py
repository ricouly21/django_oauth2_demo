from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import Account
from users.serializers import UserSerializer


class AccountSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField("get_user")

    @staticmethod
    def get_user(instance):
        serializer = UserSerializer(instance.user)
        return serializer.data

    class Meta:
        model = Account
        fields = '__all__'
