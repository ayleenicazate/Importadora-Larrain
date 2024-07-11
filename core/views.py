from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def pedidos(request):
    return render(request, 'pedidos.html')

def registro(request):
    return render(request, 'registro.html')

def menu_bodega(request):
    return render(request, 'menu_bodega.html')
