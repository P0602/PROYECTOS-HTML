from django.db import models

# Create your models here.

class Despacho(models.Model):
    numero_despacho=models.CharField(max_length=30)
    nombre_cliente=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    celular=models.CharField(max_length=12)
    productos=models.CharField(max_length=30)
    peso=models.CharField(max_length=10)
    medidas=models.CharField(max_length=17)
    fecha_ingreso=models.CharField(max_length=10)
    fecha_envio=models.CharField(max_length=10)
    estado=models.CharField(max_length=20)

