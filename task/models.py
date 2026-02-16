from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='task')
  task_name = models.CharField(max_length=255)
  create_at = models.DateTimeField(auto_now_add=True)
  is_completed = models.BooleanField(default=False)