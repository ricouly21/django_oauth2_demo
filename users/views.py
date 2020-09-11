from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.viewsets import ViewSet

from accounts.serializers import *


class UserViewSet(ViewSet):

    serializer_class = UserSerializer

    @action(methods=['POST'], detail=False)
    def get_user(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Get first matching User.
        user = User.objects.filter(
            username=username,
            email=email
        ).order_by("pk").first()

        if user:
            if user.check_password(password):
                serializer = self.serializer_class(user)
                return Response(serializer.data, status=HTTP_200_OK)
            else:
                return Response({
                    'status': HTTP_400_BAD_REQUEST,
                    "message": "ERROR: Password is incorrect.",
                }, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'status': HTTP_404_NOT_FOUND,
                "message": "ERROR: User not existing",
            }, status=HTTP_404_NOT_FOUND)

    @action(methods=['POST'], detail=False)
    def create_user(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        # Check if User is existing
        user = User.objects.filter(username=username, email=email).first()

        # If User is already existing.
        if user:
            return Response({
                'status': HTTP_400_BAD_REQUEST,
                'message': 'ERROR: User already exists.',
            }, status=HTTP_400_BAD_REQUEST)

        else:
            user = User(username=username, email=email)

            # Validate and set User password
            try:
                validate_password(password, user)
                user.set_password(password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()

            except ValidationError as e:
                return Response({
                    'status': HTTP_400_BAD_REQUEST,
                    'message': e.messages,
                }, status=HTTP_400_BAD_REQUEST)

            if user:
                serializer = self.serializer_class(user)
                return Response(serializer.data, status=HTTP_200_OK)

        return Response({
            'status': HTTP_400_BAD_REQUEST,
            'message': 'ERROR: Failed to create User',
        }, status=HTTP_400_BAD_REQUEST)



