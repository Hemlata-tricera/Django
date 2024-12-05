from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def func_base(request):
    return HttpResponse("This is Function base view")


