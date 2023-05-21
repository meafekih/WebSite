
from django.shortcuts import render
def index(request):
    return render(request, 'module/index.html')


""" 
from django.http import JsonResponse
from rest_framework import status
from .models import product


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
 """

""" 
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
    
@api_view(['GET','PUT','DELETE'])
def operations(request,pk):
    try:
        p = product.objects.get(pk=pk)
    except:
        return Response({ 
            "message" : "not Found! "
        }, status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serilizer = productSerializer(p)
        return Response(serilizer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serilizer = productSerializer(p, request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE':
        p.delete()
        return Response({ 
            "message" : "Deleted with success! "
        }, status=status.HTTP_204_NO_CONTENT)

 """


from rest_framework import generics, mixins
from .serializer import productSerializer
from .models import product
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class product_api(generics.GenericAPIView, mixins.CreateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin, mixins.RetrieveModelMixin,mixins.UpdateModelMixin):

    serializer_class = productSerializer
    queryset = product.objects.all()
    lookup_field = 'id'
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id :
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)







