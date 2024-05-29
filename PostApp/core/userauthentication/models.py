from django.db import models
from datetime import datetime

# Create your models here.
class user_db(models.Model):
     username = models.CharField(max_length=100)
     email = models.EmailField()
     password = models.CharField(max_length=128)
     confirm_password = models.CharField(max_length=128)
     profile_pic = models.ImageField(upload_to='profileimg/', blank=True, null=True)
     date=models.DateField(default=datetime.today)

    
