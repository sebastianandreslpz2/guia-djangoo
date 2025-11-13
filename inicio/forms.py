
from django import forms
from .models import Restaurante

class RestauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = ['menu', 'pedidos', 'cocina', 'reservas']
        labels = {
            'menu': 'Menú',
            'pedidos': 'Pedidos', 
            'cocina': 'Cocina',
            'reservas': 'Reservas'
        }