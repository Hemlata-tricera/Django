from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello_world(request, id):
    return HttpResponse(f"I am on Home page {id}")
    # contex = {'name': ['Hemlata', 'Yogesh']}
    # return render(request, 'index.html', contex)

def about(request):
    return HttpResponse("I am on about page")

def contact(request):
    return HttpResponse("I am on contact page")
    # contex = {'name': 'Sakshi', 'dept': 'python'}
    # return render(request, 'contact.html', contex)