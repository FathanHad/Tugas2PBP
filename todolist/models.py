from email.policy import default
from gc import is_finalized
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
