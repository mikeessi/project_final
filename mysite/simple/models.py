from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "receiver")
    content = models.TextField()
    