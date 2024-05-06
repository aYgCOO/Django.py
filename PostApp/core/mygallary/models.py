from django.db import models

# Create your models here.
class newpost(models.Model):
     caption = models.CharField(max_length=30)
     image = models.ImageField(upload_to='images/', blank=True, null=True)
     date=models.DateField( auto_now=False, auto_now_add=True)
     def __str__(self) -> str:
          return self.caption + ''
