from django.db import models

# Create your models here.
class familia(models.Model):
    equipo=models.CharField(max_length=30)
    pais=models.CharField(max_length=30)
    liga=models.CharField(max_length=30)