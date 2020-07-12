from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts.views import AccountViewSet, NoAuthViewSet, UserViewSet
from django_demo.settings import STATIC_URL, STATIC_ROOT

router = DefaultRouter()

router.register('', NoAuthViewSet, basename='no-auth-view')
router.register('users', UserViewSet, basename='users')
router.register('accounts', AccountViewSet, basename='accounts')

urlpatterns = [
    path('api/v1/', include(router.urls)),

    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    path('admin/', admin.site.urls),
]

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
