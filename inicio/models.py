from django.db import models



class Gasto(models.Model):
    Tipo = models.CharField(max_length=20)
    Articulo =  models.CharField(max_length=20)
    Cantidad = models.IntegerField()
    Precio = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f'{self.Tipo} {self.Articulo} {self.Cantidad} {self.Precio}'