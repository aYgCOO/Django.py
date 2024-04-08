from django.shortcuts import render

from django.http import HttpRequest

def home(request):
     context = {'page':'Django.Practice!'}
     return render(request, 'home/index.html', context)

def contact(request):
     context = {'page':'contact'}
     return render(request, 'home/contact.html', context)

def about(request):
     context = {'page':'about'}
     return render(request, 'home/about.html', context)
# Create your views here.
