from djnago.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]