from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
import datetime 

class OTP(models.Model):
  '''
  This is the place to store
  OTP and URL link code.
  '''
  user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='otp')
  code = models.CharField(max_length=10)
  token = models.CharField(max_length=255,unique=True)
  create_at = models.DateTimeField(auto_now_add=True)
  
  def is_valid(self):
    return timezone.now() < self.create_at + datetime.timedelta(minutes=5)