#URLS APLICACIÓN
#configurando redireccionamiento
from django.urls import path
from . import views
#creando un arreglo
urlpatterns = [
    path('',views.home, name='home'), #estamos incovando al home.html
    path('listadoGeneros/',views.listadoGeneros, name='listadoGeneros'),
    path('eliminarGenero/<id>',views.eliminarGenero, name='eliminarGenero'), #PARA LLAMAR OTRO PARAMETRO SE DEBERIA INCLUIR UN SLASH (/) Y EL NOMBRE DEL OTRO PARAMETRO
    path('nuevoGenero/', views.nuevoGenero, name='nuevoGenero'),
    path('guardarGenero', views.guardarGenero, name='guardarGenero'),
    path('editarGenero/<id>',views.editarGenero, name='editarGenero'),
    path('procesarActualizacionGenero/',views.procesarActualizacionGenero, name='procesarActualizacionGenero'),
    path('listadoPais/',views.listadoPais, name='listadoPais'),
    path("eliminarPais/<id>", views.eliminarPais, name="eliminarPais"),
    path("nuevoPais/", views.nuevoPais, name="nuevoPais"),
    path("guardarPais/", views.guardarPais, name="guardarPais"),
    path("editarPais/<id>", views.editarPais, name="editarPais"),
    path("procesarActualizacionPais/", views.procesarActualizacionPais, name="procesarActualizacionPais"),
    path('listadoDirectores/', views.listadoDirectores, name='listadoDirectores'),
    path("eliminarDirector/<id>", views.eliminarDirector, name="eliminarDirector"),
    path("nuevoDirector/", views.nuevoDirector, name="nuevoDirector"),
    path("guardarDirector/", views.guardarDirector, name="guardarDirector"),
    path("editarDirector/<id>", views.editarDirector, name="editarDirector"),
    path("procesarActualizacionDirector/", views.procesarActualizacionDirector, name="procesarActualizacionDirector"),
    path('listadoPeliculas/',views.listadoPeliculas, name='listadoPeliculas'),
    path('gestionCines/',views.gestionCines,name='gestionCines'),
    path('guardarCine/',views.guardarCine,name='guardarCine'),
    path('listadoCines/',views.listadoCines,name='listadoCines'),
    #path('guardarCine/',views.guardarCine,name='guardarCine'),pal postman
]
