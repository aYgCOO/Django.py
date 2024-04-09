from django.shortcuts import render

# Create your views here.

def recipe(request):
     if request.method == "POST":
          data = request.POST
          recipe_image = request.FILES.get('recipe_image')
          recipe_name = data.get("recipe_name")
          recipe_desc = data.get("recipe_desc")
          print(recipe_name)
          print(recipe_desc)
          print(recipe_image)
     print(data)
     return render(request, 'home/index.html')