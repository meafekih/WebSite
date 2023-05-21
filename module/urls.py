
from django.urls import path, include
from .views import product_api


urlpatterns = [
    path('<int:id>/', product_api.as_view()),
    path('', product_api.as_view())
]