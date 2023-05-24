
from django.contrib import admin
from django.urls import path, include
from module.views import index
import debug_toolbar
import allauth.account.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('module.urls')),
    path('', index, name='index'),
    path('__debug__', include(debug_toolbar.urls)),
    path('accounts/', include('allauth.urls')),
]
