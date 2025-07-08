from django.urls import path
#from .views import views
from . import views  # Importamos las vistas de la aplicación productos

app_name = 'productos' # Definimos el espacio de nombres para las URLs de la aplicación productos

urlpatterns = [ # Definimos las rutas de la aplicación productos
    path('', views.lista_productos, name='lista'), # Ruta para la lista de productos
    path('nuevo/',views.create_product, name='nuevo'), # Ruta para crear un nuevo producto
    path('editar/<int:pk>/', views.edit_product, name='editar'),  # Ruta para editar un producto existente, donde pk es la clave primaria del producto
    path('eliminar/<int:pk>/', views.delete_product, name='eliminar'),  # Ruta para eliminar un producto, donde pk es la clave primaria del producto
]
