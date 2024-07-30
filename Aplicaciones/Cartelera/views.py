from django.shortcuts import redirect,render
from .models import Genero,Pelicula,Director,Pais, Cine
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request,"home.html")

#Renderizando el template de listadoGeneros
def listadoGeneros(request):
    generosBdd = Genero.objects.all()
    return render(request, "listadoGeneros.html", {"generos": generosBdd})

#Renderizando el template de listadoPeliculas
def listadoPeliculas(request):
    peliculasBdd = Pelicula.objects.all()
    return render(request,"listadoPeliculas.html",{"peliculas": peliculasBdd})

def listadoDirectores(request):
    directoresBdd = Director.objects.all()
    return render(request,"listadoDirectores.html",{"directores": directoresBdd})

def listadoPaises(request):
    paisesBdd = Pais.objects.all()
    return render(request,"listadoPaises.html",{"paises": paisesBdd})

#Se recibe el Id para eliminar un genero
def eliminarGenero(request,id):
    generoEliminar = Genero.objects.get(id=id)
    generoEliminar.delete()
    messages.success(request,"Libro eliminado exitosamente.")
    return redirect('listadoGeneros')

#Renderizando formulario de nuevoGenero
def nuevoGenero(request):
    return render(request, 'nuevoGenero.html')

#Insertando Genero en la base de datos
def guardarGenero(request):
    nom = request.POST["nombre"]
    des = request.POST["descripcion"]
    fot = request.FILES.get("foto")
    nuevoGenero = Genero.objects.create(nombre=nom, descripcion=des, foto=fot)
    messages.success(request,"Libro registrado exitosamente.")
    return redirect('listadoGeneros')

#Renderizando formulario de actualizacion
def editarGenero(request,id):
    generoEditar = Genero.objects.get(id=id)
    return render(request,'editarGenero.html',{'generoEditar':generoEditar})

#Actualizando los nuevos datos en la BDD
def procesarActualizacionGenero(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    descripcion=request.POST['descripcion']
    generoConsultado=Genero.objects.get(id=id)
    generoConsultado.nombre=nombre
    generoConsultado.descripcion=descripcion
    generoConsultado.save()
    messages.success(request,'Genero actualizado exitosamente.')
    return redirect('listadoGeneros')





# Renderizando formulario de nuevoPais
def nuevoPais(request):
    return render(request, 'nuevoPais.html')

# Insertando Pais en la base de datos
def guardarPais(request):
    nombre = request.POST["nombre"]
    continente = request.POST["continente"]
    capital = request.POST["capital"]
    nuevoPais = Pais.objects.create(nombre=nombre, continente=continente, capital=capital)
    messages.success(request, "Pais registrado exitosamente.")
    return redirect('listadoPaises')

# Renderizando formulario de actualizacion
def editarPais(request, id):
    paisEditar = Pais.objects.get(id=id)
    return render(request, 'editarPais.html', {'paisEditar': paisEditar})

# Actualizando los nuevos datos en la BDD
def procesarActualizacionPais(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    continente = request.POST['continente']
    capital = request.POST['capital']
    paisConsultado = Pais.objects.get(id=id)
    paisConsultado.nombre = nombre
    paisConsultado.continente = continente
    paisConsultado.capital = capital
    paisConsultado.save()
    messages.success(request, 'Pais actualizado exitosamente.')
    return redirect('listadoPaises')

# Se recibe el Id para eliminar un pais
def eliminarPais(request, id):
    paisEliminar = Pais.objects.get(id=id)
    paisEliminar.delete()
    messages.success(request, "Pais eliminado exitosamente.")
    return redirect('listadoPaises')



def nuevoDirector(request):
    return render(request, 'nuevoDirector.html')

def guardarDirector(request):
    dni = request.POST["dni"]
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    estado = request.POST["estado"]
    fot = request.FILES.get("foto")
    nuevo_director = Director.objects.create(dni=dni, nombre=nombre, apellido=apellido, estado=estado, foto=fot)
    messages.success(request, "Director registrado exitosamente.")
    return redirect('listadoDirectores')

def editarDirector(request, id):
    directorEditar = Director.objects.get(id=id)
    return render(request, 'editarDirector.html', {'directorEditar': directorEditar})

def procesarActualizacionDirector(request):
    id = request.POST['id']
    dni = request.POST['dni']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    estado = request.POST['estado']
    foto = request.FILES.get('foto')
    directorConsultado = Director.objects.get(id=id)
    directorConsultado.dni = dni
    directorConsultado.nombre = nombre
    directorConsultado.apellido = apellido
    directorConsultado.estado = estado
    directorConsultado.foto = foto
    directorConsultado.save()
    messages.success(request, 'Director actualizado exitosamente.')
    return redirect('listadoDirectores')

def listadoDirectores(request):
    directores = Director.objects.all()
    return render(request, "listadoDirectores.html", {"directores": directores})

def eliminarDirector(request, id):
    directorEliminar = Director.objects.get(id=id)
    directorEliminar.delete()
    messages.success(request, "Director eliminado exitosamente.")
    return redirect('listadoDirectores')

def gestionCines(request):
    return render(request,'gestionCines.html')

#Insertando cines mediante AJAX en la Base de Datos
def guardarCine(request):
    nom=request.POST["nombre"]
    dir=request.POST["direccion"]
    tel=request.POST["telefono"]
    nuevoCine=Cine.objects.create(nombre=nom,direccion=dir,telefono=tel)    
    return JsonResponse({
        'estado': True,
        'mensaje': 'Género registrado exitosamente.'
    })

#Renderizar el listado de cines
def listadoCines(request):
    cines=Cine.objects.all()
    return render(request,'listadoCines.html', {'cines':cines})





def gestionPeliculas(request):
    return render(request,'gestionPeliculas.html')

#Insertando cines mediante AJAX en la Base de Datos
def guardarPelicula(request):
    tit=request.POST["titulo"]
    dur=request.POST["duracion"]
    sin=request.POST["sinopsis"]
    gen=request.POST["genero"]
    dir=request.POST["director"]
    pa=request.POST["pais"]
    por = request.FILES.get('portada')
    nuevaPelicula=Pelicula.objects.create(titulo=tit,duracion=dur,sinopsis=sin,genero=gen,director=dir,pais=pa,portada=por)    
    return JsonResponse({
        'estado': True,
        'mensaje': 'Pelicula registrada exitosamente.'
    })

#Renderizar el listado de cines
def listadoPeliculas(request):
    peliculas=Pelicula.objects.all()
    return render(request,'listadoPeliculas.html', {'peliculas':peliculas})