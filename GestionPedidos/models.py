from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=70)
    email = models.EmailField(blank=True, null=True)
    tel = models.CharField(max_length=8, verbose_name='Teléfono')

    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.FloatField()

    def __str__(self):
        return 'Nombre: {0}, Seccion: {1}, Precio: {2}'.format(self.nombre, self.seccion, self.precio)

class pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
