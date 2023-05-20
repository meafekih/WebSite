
from django.urls import path, include
from .views import showProduts, showProdutDetails, createProduct, deleteProduct


urlpatterns = [
    path('', showProduts, name='products'),
    path('create/', createProduct, name='createProduct'),
    path('delete/<int:pk>', deleteProduct, name='deleteProduct'),
    path('details/<int:pk>', showProdutDetails, name='productDetails')
]