from django.shortcuts import render
from .models import Pedidos
# Create your views here.
def listadoPedidos (request):
    LosPedidos=Pedidos.objects.all()
    return render(request,"GestionarPedidos.html",{"mispedidos":LosPedidos})