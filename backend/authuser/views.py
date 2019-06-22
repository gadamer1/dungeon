from django.contrib.auth.models import User
from rest_framework import viewsets,generics
from .selializers import UserSerializer,ReplySerializer
from .models import Reply
# Create your views here.

