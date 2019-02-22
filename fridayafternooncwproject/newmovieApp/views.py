# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'newmovieApp/index.html')

def base(request):
    return render(request, 'newmovieApp/base.html')

def aboutpages(request):
    return render(request, 'newmovieApp/aboutpages.html')