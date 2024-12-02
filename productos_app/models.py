from django.db import models

# Create your models here.
class Productos(models.Model):
    id_producto = models.PositiveBigIntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    marca = models.CharField(null=False, max_length=50)
    tela = models.CharField(null=False, max_length=50)
    talla = models.IntegerField()
    precio = models.FloatField(null=False)
    stock = models.PositiveIntegerField(null=False )

    def __str__(self):
        return self.nombre