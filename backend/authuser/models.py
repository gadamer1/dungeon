from django.db import models
from django.contrib.auth.models import User

class Reply(models.Model):
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    contents = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)