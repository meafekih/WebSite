
from django.urls import path, include
from .views import showProduts, operations, createProduct


urlpatterns = [
    path('', showProduts, name='products'),
    path('create/', createProduct, name='createProduct'),
    path('<int:pk>', operations, name='productDetails')
]