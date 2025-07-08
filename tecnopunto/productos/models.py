from django.db import models 

class Producto(models.Model):#Modelo para representar un producto
    #definimos los campos del modelo
    nombre = models.CharField(max_length=100, unique=True)  # Nombre del producto
    descripcion = models.TextField(blank=True)  # Descripción del producto
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio
    cantidad_stock = models.PositiveIntegerField(default=0)  # Cantidad en stock
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)  # Fecha de última actualización

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'productos'  # Nombre de la tabla en la base de datos