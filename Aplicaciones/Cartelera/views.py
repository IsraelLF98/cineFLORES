import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import redirect, render
#IMPORTO PARA TRABAJAR CON LOS OBJETOS
from .models import Cine, Director, Genero, Pais
from .models import Pelicula
from django.contrib import messages #importamos para las alerts o notificaciones
#importo el REDIRECT para la eliminación
#FUNCIÓN PARA LLAMAR A LA VISUALIZACIÓN DENTRO DE MI CARPETA TEMPLATES
def home (request):
    return render(request, "home.html")
#CREANDO LA VISTA PARA LISTADOGENERO (Renderizando)
def listadoGeneros(request):
    generosBdd=Genero.objects.all() #ESA VARIABLE generosBdd puedo ponerle el nombre que yo quiera AQUI SE APLICA EL ORM
    return render(request, "listadoGeneros.html",{'generos':generosBdd}) #aqui mando a llamar los datos de mi bdd mediante el genero : generosbdd
#PARA EL BOTON ELIMINAR (se recibe el id para eliminar un genero)
def eliminarGenero(request,id):
    generoEliminar = Genero.objects.get(id=id) #el primer ID es de la BDD y el otro ID es de los parametros de mi función
    generoEliminar.delete()
    messages.success(request,"Género eliminado exitosamente")
    return redirect('listadoGeneros') #el REDIRECT debe importarse al inicio
#RENDERIZANDO FORMULARIO DE NUEVO GENERO
def nuevoGenero(request):
    return render(request, "nuevoGenero.html")
#INSERTANDO GENEROS EN LA BASE DE DATOS
def guardarGenero(request):
    nom = request.POST["nombre"] #estas son variables locales
    des = request.POST["descripcion"] #estas son variables locales
    fot = request.FILES.get("foto") #25julio para guardar un archivo
    nuevoGenero = Genero.objects.create(nombre=nom, descripcion=des, foto=fot) #estas variables van de acuerdas a las definidas en el ID de mi frontend
    messages.success(request,"Género registrado exitosamente")
    return redirect ('listadoGeneros')
#Renderizando formulario de actualizacion
def editarGenero(request,id):
    generoEditar=Genero.objects.get(id=id)
    return render(request,'editarGenero.html',{'generoEditar':generoEditar})
#Actualizando los nuevos datos en la BDD (BOTON)
def procesarActualizacionGenero(request):
    id=request.POST["id"]
    nombre=request.POST["nombre"]
    descripcion=request.POST["descripcion"]
    generoConsultado=Genero.objects.get(id=id)
    generoConsultado.nombre=nombre
    generoConsultado.descripcion=descripcion
    generoConsultado.save()
    messages.success(request,'Genero actualizado satisfactoriamente')
    return redirect ('listadoGeneros')

#ESTO ES DIFERENTE
#CREANDO LA VISTA PARA LISTADODIRECTORES
def listadoDirectores(request):
    directoresBdd=Director.objects.all()
    return render (request, "listadoDirectores.html",{'directores':directoresBdd})
#ELIMINAR LISTADODIRECTORES
def eliminarDirector (request, id):
    directorEliminar = Director.objects.get(id=id)
    directorEliminar.delete()
    messages.success(request,"Director eliminado exitosamente")
    return redirect ('listadoDirectores')
#RENDERIZO EL FORMULARIO PARA INSERTAR EN LISTADOPAIS
def nuevoDirector(request):
    return render(request, 'nuevoDirector.html')
#FUNCIÓN PARA INSERTAR NUEVO PAIS
def guardarDirector(request):
    ced = request.POST["dni"]
    nom = request.POST["nombre"]
    ape = request.POST["apellido"]
    est = request.POST["estado"]
    fot = request.FILES.get("foto")
    nuevoDirector = Director.objects.create(dni=ced, nombre=nom, apellido=ape, estado=est, foto=fot)
    messages.success(request, "Director insertado exitosamente")
    return redirect ('listadoDirectores')
#FUNCION PARA RENDERIZAR DATOS 
def editarDirector(request,id):
    directorEditar = Director.objects.get(id=id)
    return render(request, 'editarDirector.html',{'directorEditar':directorEditar})
#ACTUALIZACION DE LOS CAMPOS DE PAIS
def procesarActualizacionDirector(request):
    id=request.POST["id"]
    dni=request.POST["dni"]
    nombre=request.POST["nombre"]
    apellido=request.POST["apellido"]
    estado=request.POST["estado"]
    foto=request.FILES.get("foto")
    directorConsultado=Director.objects.get(id=id)
    directorConsultado.dni=dni
    directorConsultado.nombre=nombre
    directorConsultado.apellido=apellido
    directorConsultado.estado=estado
    #directorConsultado.foto=foto
    #directorConsultado.save()
    if foto:
        directorConsultado.foto = foto
    directorConsultado.save()
    messages.success(request, "Director actualizado satisfactoriamente")
    return redirect('listadoDirectores')


#CREANDO LA VISTA PARA LISTADOPAIS
def listadoPais(request):
    paisBdd=Pais.objects.all()
    return render (request, "listadoPais.html",{'pais':paisBdd})
#ELIMINAR LISTADOPAIS
def eliminarPais (request, id):
    paisEliminar = Pais.objects.get(id=id)
    paisEliminar.delete()
    messages.success(request,"Pais eliminado exitosamente")
    return redirect ('listadoPais')
#RENDERIZO EL FORMULARIO PARA INSERTAR EN LISTADOPAIS
def nuevoPais(request):
    return render(request, 'nuevoPais.html')
#FUNCIÓN PARA INSERTAR NUEVO PAIS
def guardarPais(request):
    nom = request.POST["nombre"]
    con = request.POST["continente"]
    cap = request.POST["capital"]
    nuevoPais = Pais.objects.create(nombre=nom, continente=con, capital=cap)
    messages.success(request, "Genero insertado exitosamente")
    return redirect ('listadoPais')
#FUNCION PARA RENDERIZAR DATOS 
def editarPais(request,id):
    paisEditar = Pais.objects.get(id=id)
    return render(request, 'editarPais.html',{'paisEditar':paisEditar})
#ACTUALIZACION DE LOS CAMPOS DE PAIS
def procesarActualizacionPais(request):
    id=request.POST["id"]
    nombre=request.POST["nombre"]
    continente=request.POST["continente"]
    capital=request.POST["capital"]
    paisConsultado=Pais.objects.get(id=id)
    paisConsultado.nombre=nombre
    paisConsultado.continente=continente
    paisConsultado.capital=capital
    paisConsultado.save()
    messages.success(request,"Pais actualizado satisfactoriamente")
    return redirect('listadoPais')
#CREANDO LA VISTA PARA LISTADOPELICULAS
def listadoPeliculas(request):
    peliculasBdd=Pelicula.objects.all()
    return render(request, "listadoPeliculas.html",{'peliculas':peliculasBdd})

#FUNCION PARA GESTIONAR CRUD CINE (9-jul-2024)
def gestionCines(request):
    return render (request,'gestionCines.html')
#INSERTAR UN CINES CON AJAX
def guardarCine(request):
    nom=request.POST["nombre"]
    dir=request.POST["direccion"]
    tel=request.POST["telefono"]
    nuevoCine=Cine.objects.create(nombre=nom,direccion=dir,telefono=tel) #se importa el CINE
    return JsonResponse({ #ESTE JSONRESPONSE SE IMPORTA AL INICIO
        'estado': True,
        'mensaje': 'Cine registrado exitosamente'
    })
#RENDERIZAR EL LISTAO DE CINES
def listadoCines(request):
    cines = Cine.objects.all()
    return render (request,"listadoCines.html",{'cines':cines})
