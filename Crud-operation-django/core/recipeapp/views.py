from django.shortcuts import render
# Create your views here.

# def get_recipe(request):
#         if request.method == 'POST':
#              form = recipe(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('recipe_list') # type: ignore
#         else:
#              form = recipe()
#              return render(request, 'recipe_form.html', {'form': form})/


from .form import RecipeForm
def recipe_form(request):
     form = RecipeForm()
     context = {'form': form}
     return render(request, 'home/index.html', context)