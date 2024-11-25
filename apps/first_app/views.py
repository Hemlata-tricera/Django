from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello_world(request):
    return HttpResponse("<h1>I am on home page</h1>")

def about(request):
    return HttpResponse("I am on about page")

def contact(request):
    return HttpResponse("I am on contact page")