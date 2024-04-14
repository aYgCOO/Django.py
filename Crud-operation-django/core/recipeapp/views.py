from django.shortcuts import render
from .models import recipe
# from .form import chef_register
# Create your views here.


def index(request):
    if request.method == 'POST':
        print(request.POST)
        recipename = request.POST.get('recipe_name')
        recipedescription = request.POST.get('recipe_desc')
        submitbutton = request.POST.get('submit')
       

        context = {'recipe_name': recipename, 'recipe_desc': recipedescription, 'submit': submitbutton}
        return render(request, 'home/index.html', context)
    else:
        # Handle GET request (initial page load)
        context = {}
        return render(request, 'home/index.html', context)

def recipe_list(request):
    statement1 = "This is a lower case sentence."
    statement2 = "This is a uppercase sentence."
    recipe_list = recipe.objects.all()
    context = {'recipe_list': recipe_list, 'statement1': statement1, 'statement2': statement2}
    return render(request, 'home/dblisting.html', context)

# def chef(request) :
#     form = chef_register()
#     context = {'form': form}
#     return render(request, 'home/chef.html', context)
