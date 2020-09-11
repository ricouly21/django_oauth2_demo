from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase


class TestAPIStatusCheckUrls(APITestCase):
    """
    Test case for checking if the specified API URL is working properly.

    API URL: '/api/v1/check_api_status/'
    METHOD: GET
    RESPONSE_CONTENT_TYPE: 'application/json'
    """

    url_reverse = reverse('api-base-check-api-status')
    url_path = '/api/v1/check_api_status/'

    def setUp(self):
        pass

    def test_url_check_api_status(self):
        self.assertEqual(self.url_reverse, self.url_path)

    def test_url_response_check_api_status(self):
        _request = self.client.get(self.url_reverse)
        self.assertEqual(_request.status_code, HTTP_200_OK)
