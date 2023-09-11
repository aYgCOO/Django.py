from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return render(request, "index.html")


def succes_page(request):
    print("*" * 10)
    return HttpResponse("<h2>Hey this is a succes page.</h2>")
