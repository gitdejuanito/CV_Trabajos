"""tarea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,reverse_lazy
from family.views import index, listado,Crear,delete,update
from family.models import familia
from django.views.generic import CreateView
from Users.views import CrearCliente, ListarCuentas,login_view,otrosListados,CrearCustomer,listadoCustomer
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",index),
    path('admin/', admin.site.urls),
    path("create/", Crear.as_view()),
    path("delete/<int:pk>/", delete.as_view()),
    path("update/<int:pk>/", update.as_view()),
    path("listado/",listado),
    path("Crear/",CrearCliente),
    path("customer/",CrearCustomer),
    path("list-cuentas/",ListarCuentas),
    path("login/",login_view),
    path("logout/",LogoutView.as_view(template_name="logout.html")),
    path("otros/",otrosListados),
    path("list-customer",listadoCustomer),
    
]
urlpatterns +=static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)