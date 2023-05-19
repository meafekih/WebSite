from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'module/index.html')

def about(request):
    return render(request, 'module/about.html')

def showProduts(request):
    print(request)
    return HttpResponse('Hello Product')