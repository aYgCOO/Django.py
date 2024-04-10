# from django import forms
# class RecipeForm(forms.Form):
#     recipe_name = forms.CharField(label="Recipe Name", max_length=100, required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
#     recipe_desc = forms.Textarea(label="Recipe Description", required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
#     recipe_image = forms.ImageField(label="Recipe Image", required=False, widget=forms.FileInput(attrs={'class': "form-control"}))



from django.forms import ModelForm
from .models import Recipe

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name', 'recipe_desc', 'recipe_image']
        