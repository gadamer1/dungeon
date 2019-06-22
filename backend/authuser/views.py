from django.contrib.auth.models import User
from rest_framework import viewsets
from .selializers import UserSerializer,ReplySerializer
from .models import Reply
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class ReplyList(generics.ListCreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer


class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer