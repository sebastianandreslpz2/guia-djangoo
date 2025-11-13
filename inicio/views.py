from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Restaurante  
from inicio.forms import RestauranteForm  

def inicio(request):
    return render(request, 'inicio.html')

def inicio2(request):
    return render(request, 'inicio2.html')

def elaborar_comida(request):
    if request.method == 'POST':
        form = RestauranteForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('listar_comidas') 
    else:
        form = RestauranteForm()
    
    return render(request, 'elaborar_comida.html', {'form': form})

def listar_comidas(request):
    comidas = Restaurante.objects.all()
    return render(request, 'listar_comidas.html', {'listado_comidas': comidas})