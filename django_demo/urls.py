from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ViewSet

from accounts.views import AccountViewSet
from users.views import UserViewSet

from django_demo.settings import STATIC_URL, STATIC_ROOT


class APIBaseViewSet(ViewSet):
    """ Simple API status checker """
    permission_classes = []
    authentication_classes = []

    @action(methods=['GET'], detail=False)
    def check_api_status(self, request):
        return Response(
            {"status": HTTP_200_OK, "message": "API is fully functional."},
            status=HTTP_200_OK,
            content_type="application/json"
        )


""" API Router """
router = DefaultRouter()

router.register('', APIBaseViewSet, basename='api-base')
router.register('users', UserViewSet, basename='users')
router.register('accounts', AccountViewSet, basename='accounts')

""" URL patterns """
urlpatterns = [
    path('api/v1/', include(router.urls)),

    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    path('openid/', include('oidc_provider.urls', namespace='oidc_provider')),

    path('admin/', admin.site.urls),
]

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
