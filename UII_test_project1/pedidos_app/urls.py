from django.urls import path
from pedidos_app import views
urlpatterns = [
    path("",views.listadoPedidos,name="listadoPedidos")
]