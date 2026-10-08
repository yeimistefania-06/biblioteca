"""
URL configuration for gestor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from biblioteca import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crear_autor/', views.crear_autor, name='crear_autor'),
    path('editar_autor/<int:autor_id>', views.editar_autor, name='editar_autor'),
    path('eliminar_autor/<int:autor_id>', views.eliminar_autor, name='eliminar_autor'),
    path('crear_libro/', views.crear_libro, name='crear_libro'),
    path('', views.listar_libros, name='listar_libros'),
    path('editar_libro/<int:libro_id>', views.editar_libro, name='editar_libro'),
    path('eliminar_libro/<int:libro_id>', views.eliminar_libro, name='eliminar_libro'),
    path('listar_autores/',views.listar_autores,name='listar_autores'),
]
