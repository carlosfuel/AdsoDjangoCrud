from django.shortcuts import render, redirect, get_object_or_404 # Importamos las funciones necesarias de Django
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # Importamos las clases para la paginación
from .models import Producto # Importamos el modelo Producto
from .forms import ProductoForm # Importamos el formulario ProductoForm

def lista_productos(request): # Vista para listar productos
   productos_list = Producto.objects.all().order_by('-fecha_ultima_modificacion') # Obtenemos todos los productos ordenados por fecha de última modificación
   paginator = Paginator(productos_list, 10)# Paginamos la lista de productos, mostrando 10 por página
   page = request.GET.get('page', 1)# Obtenemos el número de página de la solicitud GET, por defecto es 1
   try:
       productos = paginator.page(page)   # Obtenemos la página solicitada
   except (PageNotAnInteger, EmptyPage):   # Si la página no es un número entero o está fuera de rango, devolvemos la primera página
       productos = paginator.page(1)
   return render(request, 'productos/product_list.html', {'productos': productos})  # Renderizamos la plantilla con la lista de productos

def create_product(request): # Vista para crear un nuevo producto
   form = ProductoForm(request.POST or None) # Creamos una instancia del formulario con los datos POST si existen, o None si no
   if request.method == 'POST' and form.is_valid(): # Si el método es POST y el formulario es válido
       form.save()      # Guardamos el formulario, lo que crea un nuevo producto
       return redirect('productos:lista')     # Redirigimos a la lista de productos
   return render(request, 'productos/product_form.html', {'form': form})    # Renderizamos la plantilla del formulario de producto


def edit_product(request, pk):   # Vista para editar un producto existente
   prod = get_object_or_404(Producto, pk=pk)   # Obtenemos el producto por su clave primaria (pk), o devolvemos un error 404 si no existe
   form = ProductoForm(request.POST or None, instance=prod)   # Creamos una instancia del formulario con los datos POST si existen, o None si no, y vinculamos el producto existente
   if request.method == 'POST' and form.is_valid():  # Si el método es POST y el formulario es válido
       form.save()  # Guardamos el formulario, lo que actualiza el producto existente
       return redirect('productos:lista') # Redirigimos a la lista de productos
   return render(request, 'productos/product_form.html', {'form': form}) # Renderizamos la plantilla del formulario de producto con los datos del producto existente

def delete_product(request, pk):     # Vista para eliminar un producto
   prod = get_object_or_404(Producto, pk=pk)    # Obtenemos el producto por su clave primaria (pk), o devolvemos un error 404 si no existe
   if request.method == 'POST':    # Si el método es POST, significa que se ha confirmado la eliminación
       prod.delete()   # Eliminamos el producto
       return redirect('productos:lista')   # Redirigimos a la lista de productos
   return render(request, 'productos/product_confirm_delete.html', {'producto': prod})   # Renderizamos la plantilla de confirmación de eliminación con el producto a eliminar

def inicio(request):
   """Vista para la página de inicio de TecnoPunto."""
   context = {
       'tienda': 'TecnoPunto',
       'descripcion': 'Venta de productos tecnológicos',
   }
   return render(request, 'base.html', context)

def inicio(request):
   context = {'tienda': 'TecnoPunto', 'descripcion': 'Venta de productos tecnológicos'}
   return render(request, 'inicio.html', context)