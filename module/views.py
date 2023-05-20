from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import product


def index(request):
    return render(request, 'module/index.html')

def showProduts2(request):
    data = product.objects.all()
    result = list(data.values())
    return JsonResponse({
        'books':result
    })

def showProdutDetails(request, pk):
    data = product.objects.filter(id=pk).values()
    result = list(data.values())
    return JsonResponse({
        'book':result
    })


from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import product
from .serializer import productSerializer

@api_view(['GET'])
def showProduts(request):
    books = product.objects.all()
    serializer = productSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createProduct(request):
    serializer = productSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors) 
    
@api_view(['DELETE'])
def deleteProduct(request,pk):
    p = product.objects.get(id=pk)
    p.delete()
    return JsonResponse({ 
        "message" : "Deleted with success! "
    })