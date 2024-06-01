from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profileimg/', blank=True, null=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
