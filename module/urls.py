
from django.urls import path, include
from .views import showProduts


urlpatterns = [
    path('', showProduts, name='products')
]