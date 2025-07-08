from django.contrib import admin # Importa la clase admin para el panel de administración
from django.urls import path,include # Importa las funciones path e include para definir las rutas
from productos.views import inicio # Importa la vista de inicio desde el módulo productos.views


urlpatterns = [
   path('admin/', admin.site.urls), # ruta para el panel de administración
   path('', inicio, name='inicio'), #ruta para la página de inicio
   path('productos/', include('productos.urls')),  # ruta para las vistas de productos
]

