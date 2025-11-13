from django.urls import path
from inicio.views import inicio, inicio2, elaborar_comida, listar_comidas

urlpatterns = [
    path('', inicio, name='inicio'),
    path('inicio2/', inicio2, name='inicio2'),
    path('elaborar-comida/', elaborar_comida, name='elaborar_comida'),  # ← SIN parámetros
    path('listar-comidas/', listar_comidas, name='listar_comidas'),
]