from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    peoples = [
        {"name": "Ayanabha", "age": 19, "role": "Frontend"},
        {"name": "Agnik", "age": 21, "role": "Backend"},
        {"name": "Avishake", "age": 16, "role": "Nothing"},
        {"name": "Vivek", "age": 22, "role": "Backend-Assistent"},
        {"name": "Supriya", "age": 18, "role": "Frontend-Assistent"},
    ]
    veg = ["Potato", "Ginger", "Cucumbe"]
    for people in peoples:
        print(people)
    return render(request, "home/index.html", context={"peoples": peoples, "veg":veg})


def succes_page(request):
    print("*" * 10)
    return HttpResponse("<h2>Hey this is a succes page.</h2>")

def about(request):
    return render(request, "home/about.html")
def contact(request):
    return render(request, "home/contact.html")



