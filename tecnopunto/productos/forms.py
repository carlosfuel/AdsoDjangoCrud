from django import forms # Importamos el módulo forms de Django
from .models import Producto # Importamos el modelo Producto desde el archivo models.py

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad_stock'] # Especificamos los campos que queremos incluir en el formulario