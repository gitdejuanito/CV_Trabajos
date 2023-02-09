from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from Users.models import customer

class CustomerForm(ModelForm):
    class Meta:
        model=customer
        fields="__all__"
        exclude=["user"]


class CreateCustomer(forms.Form):
    Username=forms.CharField(max_length=25)
    name=forms.CharField(max_length=25)
    

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2",]







