"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import routers
from django.urls import path,include
from authuser import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('reply_detail',views.ReplyDetail)
router.register('reply_list',views.ReplyList)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/',admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
]
