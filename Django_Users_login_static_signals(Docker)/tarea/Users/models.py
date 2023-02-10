from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.



class customer(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    Username=models.CharField(max_length=25)
    name=models.CharField(max_length=25)
    profile_pic=models.ImageField(default= "profile.png", null=True, blank=True)
    
    
##signals 
def create_profile(sender,instance,created, **kwargs):
    if created:
        customer.objects.create(user=instance)
        print("USER creado")
post_save.connect(create_profile, sender=User)