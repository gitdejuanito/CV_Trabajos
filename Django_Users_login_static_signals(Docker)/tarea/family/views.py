from django.shortcuts import render
from django.http import HttpResponse
from family.models import familia
from family.forms import familiaForm
from django.contrib.auth.decorators import login_required
from family.decorators import allowed_users
from Users.models import customer
from django.contrib.auth.mixins import LoginRequiredMixin



from django.views.generic import CreateView, DeleteView, UpdateView
# Create your views here.
def index(request):
    return render(request,"base.html",context={})


@allowed_users(allowed_roles=("customers"))
@login_required
def listado(request):
    datos=familia.objects.all()
    context={"datos":datos}
    return render(request, "listado.html",context=context)


class Crear(CreateView):
    model=familia
    fields="__all__"
    success_url="/listado/"

class delete(DeleteView):
    model=familia
    fields="__all__"
    template_name="delete.html"
    success_url="/listado/"


class update(UpdateView):
    model=familia
    fields="__all__"
    template_name="update.html"
    success_url="/listado/"


    

