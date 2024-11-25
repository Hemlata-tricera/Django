from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def demo1(request):
    return HttpResponse("<h1 style='color:red'>I am on demo1 page</h1><hr><p>This is the paragraph of our page</p><style></style>")

def demo2(request):
    return HttpResponse("<h1>I am on demo2 page</h1>")
def demo3(request):
    return HttpResponse("<h1>I am on demo3 page</h1>")

