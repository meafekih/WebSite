
from django.urls import path, include
from .views import showProduts, showProdutDetails


urlpatterns = [
    path('', showProduts, name='products'),
    path('details/', showProdutDetails, name='productDetails')
]