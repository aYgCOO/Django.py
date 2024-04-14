# from django import forms
# class RecipeForm(forms.Form):
#     recipe_name = forms.CharField(label="Recipe Name", max_length=100, required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
#     recipe_desc = forms.Textarea(label="Recipe Description", required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
#     recipe_image = forms.ImageField(label="Recipe Image", required=False, widget=forms.FileInput(attrs={'class': "form-control"}))



from django.forms import ModelForm
from .models import Recipe
# from django import forms

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name', 'recipe_desc', 'recipe_image']

# class ChefRegister(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     phone = forms.IntegerField()
#     age = forms.IntegerField()
#     gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')])
#     city = forms.CharField(max_length=60)
#     about = forms.CharField(widget=forms.Textarea)



    
        