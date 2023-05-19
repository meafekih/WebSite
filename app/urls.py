
from django.contrib import admin
from django.urls import path, include
from module.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('module.urls')),
    path('', index, name='index'),
]
