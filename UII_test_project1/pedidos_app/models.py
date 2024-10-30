from django.db import models

# Create your models here.
class Pedidos(models.Model):
    id_pedido=models.CharField(primary_key=True,max_length=6)
    id_cliente=models.CharField(max_length=6)
    fecha_pedido=models.CharField(max_length=50)
    total_pedido=models.CharField(max_length=50)
    estado_pedido=models.CharField(max_length=50)
    metodo_pago=models.CharField(max_length=50)
    fecha_entrega=models.CharField(max_length=50)
    metodo_entrega=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.id_pedido