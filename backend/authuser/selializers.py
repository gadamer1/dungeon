from django.contrib.auth.models import User
from rest_framework import serializers
from .models import  Reply

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = User
        fields= ('username','email','is_staff')


class ReplySerializer(serializers.ModelSerializer):
    class meta:
        model = Reply
        fields = ('writer','created_date','contents')