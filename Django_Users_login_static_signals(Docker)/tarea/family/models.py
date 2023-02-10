from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class familia(models.Model):
    
    equipo=models.CharField(max_length=30,verbose_name="Nombre del equipo")
    pais=models.CharField(max_length=30)
    liga=models.CharField(max_length=30)

    #---->SIRVE PARA DAR NOMBRE EN DJANGO ADMIN
    def __str__ (self):
        return self.equipo

