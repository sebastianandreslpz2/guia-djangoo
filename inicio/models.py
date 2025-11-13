from django.db import models

class Restaurante(models.Model):  # ← CAMBIADO de Comida a Restaurante
    menu = models.CharField(max_length=100)
    pedidos = models.CharField(max_length=100)
    cocina = models.CharField(max_length=100)
    reservas = models.CharField(max_length=100)

    def __str__(self):
        return self.menu