
from django.contrib import admin
from django.urls import path, include
from module.views import index, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('module.urls')),
    path('', index, name='index'),
    path('about/', about, name='about')
]
