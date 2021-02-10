"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name = "index"),
    path('listar_cursos', views.listar_cursos, name="listar_cursos"),
    path('eliminar_curso/<int:id>',views.eliminar_curso, name="eliminar_curso"),
    path('save_curso/',views.save_curso, name="save_curso"),
    path('crear_curso/',views.crear_curso, name="crear_curso"),

    
    path('crear_carrera/<str:titulo>/<str:contenido>/<str:publicado>',views.crear_carrera, name="crear_carrera"),
    path('listar_carreras', views.listar_carreras, name="listar_carreras"),
    path('create-carrera/',views.create_carrera, name="create_carrera"),
    path('buscar_carrera',views.buscar_carrera, name="buscar_carrera"),
    path('editar_carrera/<int:id>',views.editar_carrera, name="editar_carrera"),
    path('eliminar_carrera/<int:id>',views.eliminar_carrera, name="eliminar_carrera"),
    path('save-carrera/',views.save_carrera, name="save_carrera"),

]
