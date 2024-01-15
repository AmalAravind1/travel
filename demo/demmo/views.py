from django.http import HttpResponse
from django.shortcuts import render
from .models import place, place2


# Create your views here.
def index(request):
    obj=place.objects.all()
    obj1=place2.objects.all()
    return render(request, 'index.html',{'result':obj,'result1':obj1})


# def about(request):
#     return render(request,'about.html')
# def contact(request):
#     return HttpResponse('this is contact page')
# def details(request):
#     return render(request,'details.html')
# def thanks(request):
#     return HttpResponse('thank you')
# def calc(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     add = x + y
#     multi = x * y
#     div = x / y
#     sub = x - y
#     return render(request, 'reslt.html', {"addition": add, "multiplication": multi, "division": div,
#                   "subs": sub})
