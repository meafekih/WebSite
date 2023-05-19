from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'module/index.html')

def showProduts(request):
    return render(request, 'module/products.html')

def showProdutDetails(request):
    return render(request, 'module/details.html')
