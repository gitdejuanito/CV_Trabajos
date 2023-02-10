from django.shortcuts import render
from Users.models import customer
from django.contrib.auth import login,  authenticate
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Users.forms import CreateUserForm,CreateCustomer, CustomerForm
from family.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group



def CrearCustomer(request):
    if request.method==("GET"):
        form=CreateCustomer()
        context={
            "form":form
        }
        return render(request,"CreateCustomer.html",context=context)
    
    elif request.method==("POST"):
        form=CreateCustomer(request.POST)
        if form.is_valid():
            
            customer.objects.create(
                Username=form.cleaned_data["Username"], 
                name=form.cleaned_data["name"],
            


            )
        
        context={"form":form}
            
        return render(request,"CreateCustomer.html",context={}) and HttpResponse("Customer creado")

def listadoCustomer(request):
    customers=customer.objects.all()
    context={"customers":customers}
    return render(request,"listadoCustomer.html",context=context)



# Create your views here.

def CrearCliente(request):
    if request.method==("GET"):
        form=CreateUserForm()
        context={
            "form":form
        }
        return render(request,"CuentaForm.html",context=context)

    elif request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
           
            user=form.save()
            context={"form":form}
            group=Group.objects.get(name="customers")
            user.groups.add(group)

            
            
        return render(request,"CuentaForm.html",context={}) and HttpResponse("Cuenta creada")


@login_required
def ListarCuentas(request):
    all_products=customer.objects.all()
    
    context={
        "all_products":all_products
    }
    return render(request,"list-cuentas.html",context=context)

def login_view(request):
    if request.method=="GET":
        form=AuthenticationForm()
        context={"form":form}
        return render(request,"login.html",context=context)

    elif request.method=="POST":
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")

            user=authenticate( username=username, password=password)

            if user is not None:
                login(request,user)
                context={
                    "message":f"Hola {username}"
                }
                return render(request,"base.html",context=context)
        
        form=AuthenticationForm()
        context={
            "form":form,
            "errors":"username or password incorrrect"
        }
        return render(request,"login.html", context=context)

@login_required
@allowed_users(allowed_roles=["admin"])
def otrosListados(request):
    return render(request,"otros.html",context={})


