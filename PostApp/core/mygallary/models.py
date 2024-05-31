from django.db import models
from userauthentication.models import user_db

# Create your models here.
class newpost(models.Model):
     user = models.ForeignKey(user_db, on_delete=models.CASCADE)
     caption = models.CharField(max_length=30)
     image = models.ImageField(upload_to='images/', blank=True, null=True)
     date=models.DateField( auto_now=False, auto_now_add=True)
     def __str__(self) -> str:
          return self.caption + ''
