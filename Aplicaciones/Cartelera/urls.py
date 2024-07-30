#Aplicacion de la Cartelera 


# Configurando redireccionamiento
from django.urls import path

# Importando todas las vistas de Cartelera

from . import views

#Crear un arreglo para llamar al HTML que se creo para listar las bases de datos.

urlpatterns = [
    path('',views.home),
    
    # GENERO
    
    # Ruta que no tiene parámetro

    path('listadoGenero/',views.listadoGenero, name='listadoGenero'),
    
    # Ruta que si tiene parámetro de id que vamos a exportar, esta funcion se llama (RestFull)

    path('eliminarGenero/<id>',views.eliminarGenero, name='eliminarGenero'),
    path('nuevoGenero/',views.nuevoGenero, name='nuevoGenero'),
    path('guardarGenero/',views.guardarGenero, name='guardarGenero'),
    path('editarGenero/<id>',views.editarGenero, name='editarGenero'),
    path('procesarActualizacionGenero',views.procesarActualizacionGenero, name='procesarActualizacionGenero'),
    
    # ---------------------------------------------------------------------------------------------------------------------
    
    # DIRECTOR

    path('listadoDirector/',views.listadoDirector, name='listadoDirector'),
    path('guardarDirector/',views.guardarDirector, name='guardarDirector'),
    path('eliminarDirector/<id>',views.eliminarDirector, name='eliminarDirector'),
    path('nuevoDirector/',views.nuevoDirector, name='nuevoDirector'),
    
    
    # EDITAR DE LA TABLA DDE DIRECTOR
    
    path('editarDirector/<id>',views.editarDirector, name='editarDirector'),
    path('procesarActualizacionDirector',views.procesarActualizacionDirector, name='procesarActualizacionDirector'),
    
    # ---------------------------------------------------------------------------------------------------------------------
    
    # PELICULAS

    path('listadoPelicula/',views.listadoPelicula, name='listadoPelicula'),
    path('guardarPelicula/',views.guardarPelicula, name='guardarPelicula'),
    path('eliminarPelicula/<id>',views.eliminarPelicula, name='eliminarPelicula'),
    path('nuevoPelicula/',views.nuevoPelicula, name='nuevoPelicula'),
    
    
    # EDITAR DE LA TABLA DDE Peliculas
    
    path('editarPelicula/<id>',views.editarPelicula, name='editarPelicula'),
    path('procesarActualizacionPelicula',views.procesarActualizacionPelicula, name='procesarActualizacionPelicula'),
    
    # ---------------------------------------------------------------------------------------------------------------------
    
    # PAISES

    path('listadoPais/',views.listadoPais, name='listadoPais'),
    path('guardarPais/',views.guardarPais, name='guardarPais'),
    path('eliminarPais/<id>',views.eliminarPais, name='eliminarPais'),
    path('nuevoPais/',views.nuevoPais, name='nuevoPais'),
    
    
    # EDITAR DE LA TABLA DDE Paises
    
    path('editarPais/<id>',views.editarPais, name='editarPais'),
    path('procesarActualizacionPais',views.procesarActualizacionPais, name='procesarActualizacionPais'),


    # ---------------------------------------------------------------------------------------------------------------------
    path('gestionCines/',views.gestionCines, name='gestionCines'),
    path('guardarCine/',views.guardarCine, name='guardarCine'),
    path('listadoCines/',views.listadoCines, name='listadoCines'),

    #Pelicula 
    path('gestionPeliculas/',views.gestionPeliculas, name='gestionPeliculas'), 
    path('guardarPelicula/',views.guardarPelicula, name='guardarPelicula'), 
    path('listadoPeliculas/',views.listadoPeliculas, name='listadoPeliculas'), 


]   