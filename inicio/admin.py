from django.contrib import admin
from .models import Restaurante

@admin.register(Restaurante)
class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('menu', 'pedidos', 'cocina', 'reservas')
