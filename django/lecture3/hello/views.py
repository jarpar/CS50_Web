from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello, world! TEST")

def jarek(request):
    return HttpResponse("Hello, Jarek!")

def greet(request, name):
    return render(request, "hello/greet/html"), {
        "name": name.capitalize()
    }

def index(request):
    return render(request="hello/index.html")

