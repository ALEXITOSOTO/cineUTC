# Configurando rediccionamiento
from django.urls import path
from . import views #Importando todas las vistas de views

urlpatterns = [
    path('', views.home, name='home'),
    path('gestionPeliculas/', views.gestionPeliculas, name='gestionPeliculas'),
    path('guardarPelicula/', views.guardarPelicula, name='guardarPelicula'),
    path('listadoPeliculas/', views.listadoPeliculas, name='listadoPeliculas'),

    path('listadoGeneros/', views.listadoGeneros, name='listadoGeneros'),
    path('nuevoGenero/', views.nuevoGenero, name='nuevoGenero'),
    path('guardarGenero/', views.guardarGenero, name='guardarGenero'),
    path('editarGenero/<id>/', views.editarGenero, name='editarGenero'),
    path('procesarActualizacionGenero/', views.procesarActualizacionGenero, name='procesarActualizacionGenero'),
    path('eliminarGenero/<id>/', views.eliminarGenero, name='eliminarGenero'),
    
    path('listadoPaises/', views.listadoPaises, name='listadoPaises'),
    path('nuevoPais/', views.nuevoPais, name='nuevoPais'),
    path('guardarPais/', views.guardarPais, name='guardarPais'),
    path('editarPais/<id>/', views.editarPais, name='editarPais'),
    path('procesarActualizacionPais/', views.procesarActualizacionPais, name='procesarActualizacionPais'),
    path('eliminarPais/<id>/', views.eliminarPais, name='eliminarPais'),

    path('listadoDirectores/', views.listadoDirectores, name='listadoDirectores'),
    path('nuevoDirector/', views.nuevoDirector, name='nuevoDirector'),
    path('guardarDirector/', views.guardarDirector, name='guardarDirector'),
    path('editarDirector/<id>/', views.editarDirector, name='editarDirector'),
    path('procesarActualizacionDirector/', views.procesarActualizacionDirector, name='procesarActualizacionDirector'),
    path('eliminarDirector/<id>/', views.eliminarDirector, name='eliminarDirector'),

    path('gestionCines/', views.gestionCines, name='gestionCines'),
    path('guardarCine/', views.guardarCine, name='guardarCine'),
    path('listadoCines/', views.listadoCines, name='listadoCines'),
]

