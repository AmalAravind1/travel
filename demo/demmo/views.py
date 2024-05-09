from django.http import HttpResponse
from django.shortcuts import render
from .models import place, place2


# Create your views here.
def index(request):
    obj=place.objects.all()
    obj1=place2.objects.all()
    return render(request, 'index.html',{'result':obj,'result1':obj1})



