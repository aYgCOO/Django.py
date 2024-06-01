from django.contrib import admin
from userauthentication.models import UserDetails

# Register your models here.
from .models import *
admin.site.register(UserDetails)
