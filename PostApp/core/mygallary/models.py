from django.db import models
from userauthentication.models import User 
from django.utils import timezone
 # Ensure this import works, else it should be from django.contrib.auth.models import User

class newpost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=30)
    image_file = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)  # Set to auto_now_add to automatically set the timestamp
    def __str__(self) -> str:
        return f"{self.user.username} - {self.caption[:20]}"  # Use self.user.username instead of self.User.username
