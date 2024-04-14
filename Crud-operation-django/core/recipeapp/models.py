from django.db import models
from django.contrib import admin

# Create your models here.
class recipe(models.Model):
     recipe_name = models.CharField(max_length=100)
     recipe_desc = models.TextField()
     def __str__(self):
        return self.recipe_name + '' + self.recipe_desc 

admin.site.register(recipe)

# class chef_list(models.Model):
#     chef_name = models.CharField(max_length=100)
#     chef_about = models.TextField()
    

    

