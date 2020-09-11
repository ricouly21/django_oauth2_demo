from datetime import timedelta

from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from oauth2_provider.models import Application, AccessToken
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.test import APITestCase, APIRequestFactory


class TestUserUrls(APITestCase):
    """
    Test case for checking if the specified API URL is working properly.

    API URL: /api/v1/users/get_user/
    METHOD: POST
    RESPONSE_CONTENT_TYPE: 'application/json'
    """

    factory = APIRequestFactory()
    url_reverse = reverse('users-get-user')
    url_path = '/api/v1/users/get_user/'

    def initialize_model_instances(self):
        """
        Here we initialize all model instances that we will need for the test case functions.
        """
        self.user_info = {"username": "test_user", "email": "test_user@test.com"}
        self.user_password = "p@ssw0rD1"

        # Initialize user instance
        self.user = User.objects.create(**self.user_info)
        self.user.set_password(self.user_password)
        self.user.save()

        # Initialize an OAuth2 application instance
        self.application = Application.objects.create(
            user=self.user,
            name="TestApplication",
            client_type="confidential",
            authorization_grant_type="password",
        )

        # Initialize an OAuth2 access token instance
        self.access_token = AccessToken.objects.create(
            user=self.user,
            application=self.application,
            token="test_token",
            scope="read write",
            expires=now() + timedelta(hours=1)
        )

        # Set access token to client request header
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.access_token.token)

    def setUp(self):
        self.initialize_model_instances()

    def test_url_users_get_user(self):
        self.assertEqual(self.url_reverse, self.url_path)

    def test_url_response_users_get_user_success(self):
        payload = self.user_info
        payload["password"] = self.user_password

        _request = self.client.post(self.url_reverse, payload)

        self.assertEqual(_request.status_code, HTTP_200_OK)
        self.assertEqual(_request.data.get('username'), self.user_info.get('username'))
        self.assertEqual(_request.data.get('email'), self.user_info.get('email'))

    def test_url_response_users_get_user_incorrect_password(self):
        payload = self.user_info
        payload["password"] = 'incorrectPassword'

        _request = self.client.post(self.url_reverse, payload)

        self.assertEqual(_request.status_code, HTTP_400_BAD_REQUEST)

    def test_url_response_users_get_user_not_found(self):
        payload = {
            "username": "unknown_user",
            "email": "unknown_user@test.com",
            "password": "p@ssw0rD1"
        }

        _request = self.client.post(self.url_reverse, payload)

        self.assertEqual(_request.status_code, HTTP_404_NOT_FOUND)

