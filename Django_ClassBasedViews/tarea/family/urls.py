from django.contrib import admin
from django.urls import path
from family.views import index,listado

urlpatterns = [
    path("",index),
    path('admin/', admin.site.urls),
    path("listado/",listado),
]