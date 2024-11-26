from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def demo1(request, id):
    context = {
    'cars': [
      {
        'brand': 'Ford',
        'model': 'Mustang',
        'year': '1964',
      },
      {
        'brand': 'Ford',
        'model': 'Bronco',
        'year': '1970',
      },
      {
        'brand': 'Volvo',
        'model': 'P1800',
        'year': '1964',
      }]
    }
    return render(request, 'demo1.html', context)
    # return HttpResponse(f"<h1 style='color:red'>I am on demo1 page{id}</h1><hr><p>This is the paragraph of our page</p><style></style>")

def demo2(request):
    context = {'name': 'Vishakha'}
    return render(request, 'demo2.html', context)
def demo3(request):
    return HttpResponse("<h1>I am on demo3 page</h1>")

