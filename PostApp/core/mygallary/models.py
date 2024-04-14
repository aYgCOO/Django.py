from django.db import models

# Create your models here.
class newpost(models.Model):
     caption = models.CharField(max_length=60)
     image = models.ImageField(upload_to='images/', blank=True, null=True)
     def __str__(self) -> str:
          return self.caption + '' + self.image
