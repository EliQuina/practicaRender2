from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Genero, Director,Peliculas, Pais, Cine

# Importar los mensajes (Alert)

from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


#Renderiza nuestra página con home.html --> la cual se encuentra en la carpeta de Templates

def home(request):
    return render(request,"home.html")
 
#Renderizando el Template  de listadoGenero

def listadoGenero(request):
    
    #Crear un objeto para crear la base de datos y obtener datos
    
    generosBdd = Genero.objects.all()
    return render(request,"listadoGenero.html",
                  {'generos' :generosBdd})

#Se recibe el id para eliminar un género
# El primer id = Modelo - id = Parametro
def eliminarGenero(request, id):
    generoeliminar = Genero.objects.get(id=id)
    generoeliminar.delete()
    messages.success(request,"Género Eliminado Exitosamente.")
    return redirect('listadoGenero')

 

def listadoDirector(request):
    
    #Crear un objeto para crear la base de datos y obtener datos
    
    directorBdd = Director.objects.all()
    return render(request,"listadoDirector.html",
                  {'directores' :directorBdd})

def listadoPelicula(request):
    
    #Crear un objeto para crear la base de datos y obtener datos
    
    peliculaBdd = Peliculas.objects.all()
    return render(request,"listadoPelicula.html",
                  {'peliculas' :peliculaBdd})
    
#Renderizando formulario de nuevo genero
    
def nuevoGenero(request):
   return render(request,'nuevoGenero.html')

#Insertando generos en la base de datos
    
def guardarGenero(request):
   nom = request.POST["nombre"]
   des = request.POST["descripcion"]
   fot = request.FILES.get("foto")
   nuevoGenero = Genero.objects.create(nombre=nom, descripcion=des, foto=fot)
   messages.success(request,"Género Registrado Exitosamente.")
   return redirect('listadoGenero')

#Renderizar formularios de actualizacion

def editarGenero(request,id):
    generoEditar=Genero.objects.get(id=id)
    return render(request,'editarGenero.html',{'generoEditar': generoEditar})

#Actualizar los nuevos datos en la BDD

def procesarActualizacionGenero(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    descripcion=request.POST['descripcion']
    foto = request.FILES.get("foto")
    generoConsultado=Genero.objects.get(id=id)
    generoConsultado.nombre=nombre
    generoConsultado.descripcion=descripcion
    generoConsultado.foto=foto
    generoConsultado.save()
    messages.success(request,"El Género se ha actualizado correctamente")
    return redirect('listadoGenero')

#---------------------------------------------------------------------------------------------------------------------

# DIRECTOR

#Insertando generos en la base de datos
    
def guardarDirector(request):
   d = request.POST["dni"]
   apell = request.POST["apellido"]
   nomb = request.POST["nombre"]
   est = request.POST["estado"]
   fot = request.FILES.get("foto")
   nuevoDirector = Director.objects.create(dni=d,apellido=apell,nombre=nomb,estado=est,foto=fot)
   messages.success(request,"Director Registrado Exitosamente.")
   return redirect('listadoDirector')

#Actualizar El modelo de Director 

def editarDirector(request,id):
    directorEditar=Director.objects.get(id=id)
    directores = Director.objects.all()
    return render(request,'editarDirector.html',{'directorEditar': directorEditar, 'directores':directores})

#Se recibe el id para eliminar un género
# El primer id = Modelo - id = Parametro
def eliminarDirector(request, id):
    directoreliminar = Director.objects.get(id=id)
    directoreliminar.delete()
    messages.success(request,"Director Eliminado Exitosamente.")
    return redirect('listadoDirector')

#Renderizando formulario de nuevo genero
    
def nuevoDirector(request):
   return render(request,'nuevoDirector.html')


#Actualizar los nuevos datos en la BDD

def procesarActualizacionDirector(request):
    id=request.POST['id']
    dni=request.POST['dni']
    apellido=request.POST['apellido']
    nombre=request.POST['nombre']
    estado=request.POST['estado']
    foto= request.FILES.get('foto')
    directorConsultado=Director.objects.get(id=id)
    directorConsultado.dni=dni
    directorConsultado.apellido=apellido
    directorConsultado.nombre=nombre
    directorConsultado.estado=estado
    directorConsultado.foto=foto
    directorConsultado.save()
    messages.success(request,"El Director se ha actualizado correctamente")
    return redirect('listadoDirector')

#---------------------------------------------------------------------------------------------------------------------

# PELICULAS

def guardarPelicula(request):
   ti = request.POST["titulo"]
   du = request.POST["duracion"]
   si = request.POST["sinopsis"]
   ge_id = request.POST["genero"]
   ge = Genero.objects.get(id=ge_id)
   dire_id = request.POST["director"]
   dire = Director.objects.get(id=dire_id)
   nuevaPelicula = Peliculas.objects.create(titulo=ti,duracion=du,sinopsis=si,genero=ge,director=dire)
   messages.success(request,"Película Registrada Exitosamente.")
   return redirect('listadoPelicula')


#Actualizar El modelo de Director 

def editarPelicula(request,id):
    peliculaEditar=Peliculas.objects.get(id=id)
    generos = Genero.objects.all()
    directores = Director.objects.all()
    return render(request,'editarPelicula.html',{'peliculaEditar': peliculaEditar, 'generos': generos, 'directores': directores})

#Se recibe el id para eliminar un género
# El primer id = Modelo - id = Parametro
def eliminarPelicula(request, id):
    peliculaeliminar = Peliculas.objects.get(id=id)
    peliculaeliminar.delete()
    messages.success(request,"Pelicula Eliminada Exitosamente.")
    return redirect('listadoPelicula')

#Renderizando formulario de nuevo genero
    
def nuevoPelicula(request):
   generos = Genero.objects.all()
   directores = Director.objects.all()
   return render(request,'nuevoPelicula.html', {'generos': generos, 'directores': directores})


#Actualizar los nuevos datos en la BDD

def procesarActualizacionPelicula(request):
    id=request.POST['id']
    titulo=request.POST['titulo']
    duracion=request.POST['duracion']
    sinopsis=request.POST['sinopsis']
    genero_id=request.POST['genero']
    genero = Genero.objects.get(id=genero_id)
    director_id=request.POST['director']
    director = Director.objects.get(id=director_id)
    peliculaConsultado=Peliculas.objects.get(id=id)
    peliculaConsultado.titulo=titulo
    peliculaConsultado.duracion=duracion
    peliculaConsultado.sinopsis=sinopsis
    peliculaConsultado.genero=genero
    peliculaConsultado.director=director
    peliculaConsultado.save()
    messages.success(request,"La Película se ha actualizado correctamente")
    return redirect('listadoPelicula')

#---------------------------------------------------------------------------------------------------------------------

# PAIS

def listadoPais(request):
    
    #Crear un objeto para crear la base de datos y obtener datos
    
    PaisBdd = Pais.objects.all()
    return render(request,"listadoPais.html",
                  {'paises' :PaisBdd})

def guardarPais(request):
   nom = request.POST["nombre"]
   con = request.POST["continente"]
   cap = request.POST["capital"]
   nuevoPais = Pais.objects.create(nombre=nom,continente=con,capital=cap)
   messages.success(request,"País Registrado Exitosamente.")
   return redirect('listadoPais')

#Actualizar El modelo de Director 

def editarPais(request,id):
    paisEditar=Pais.objects.get(id=id)
    return render(request,'editarPais.html',{'paisEditar': paisEditar})

#Se recibe el id para eliminar un género
# El primer id = Modelo - id = Parametro
def eliminarPais(request, id):
    paiseliminar = Pais.objects.get(id=id)
    paiseliminar.delete()
    messages.success(request,"País Eliminado Exitosamente.")
    return redirect('listadoPais')

#Renderizando formulario de nuevo genero
    
def nuevoPais(request):
   return render(request,'nuevoPais.html')


#Actualizar los nuevos datos en la BDD

def procesarActualizacionPais(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    continente=request.POST['continente']
    capital=request.POST['capital']
    paisConsultado=Pais.objects.get(id=id)
    paisConsultado.nombre=nombre
    paisConsultado.continente=continente
    paisConsultado.capital=capital
    paisConsultado.save()
    messages.success(request,"El Pís se ha actualizado correctamente")
    return redirect('listadoPais')
    
#Funcion para gestionar el CRUD de Cine
def gestionCines(request):
    return render(request,"gestionCines.html")    

#Insertando cines mediante AJAX en la base de datos 
@csrf_exempt
def guardarCine(request):
    nombre=request.POST["nombre"]
    dir=request.POST["direccion"]
    tel=request.POST["telefono"]
    nuevoCine=Cine.objects.create(nombre=nombre,direccion=dir,telefono=tel)    
    messages.success(request,"Cine registrado exitosamente.")
    return JsonResponse({
      'estado': True,
        'mensaje': 'Género registrado exitosamente.'
    })
#Renderizar el listado de cines
def listadoCines(request):
    cines=Cine.objects.all()
    return render(request,"listadoCines.html", {'cines':cines})

#PELICULA
def gestionPeliculas(request):
    director = Director.objects.all()
    genero = Genero.objects.all()
    return render(request,'gestionPelicula.html',{'directores':director,'generos':genero})

#Insertando cines mediante FETCH en la Base de Datos
@csrf_exempt
def guardarPelicula(request):
    tit = request.POST["titulo"]
    dur = request.POST["duracion"]
    sip = request.POST["sinopsis"]

    gen = request.POST["genero"]
    genero_instancia = Genero.objects.get(id=gen)

    dir = request.POST["director"]
    director_instancia = Director.objects.get(id=dir)

    nuevaPelicula = Peliculas.objects.create(
        titulo=tit, duracion=dur, sinopsis=sip,
        genero=genero_instancia, director=director_instancia
    )

    return JsonResponse({
        'estado': True,
        'mensaje': 'Película registrada exitosamente.'
    })
    
def listadoPeliculas(request):
    peliculasBdd=Peliculas.objects.all()
    return render(request,"listadoPelicula.html", {'peliculas':peliculasBdd})

#DIRECTOR
def gestionDirectores(request):
    return render(request,'gestionDirector.html')

#Insertando cines mediante AJAX en la Base de Datos
#CON AJAX
# @csrf_exempt
# def guardarDirector(request):
#     dni=request.POST["dni"]
#     ape=request.POST["apellido"]
#     nom=request.POST["nombre"]
#     es = 'estado' in request.POST and request.POST['estado']=='on'
#     fot=request.FILES.get("foto")
#     nuevoDirector=Director.objects.create(dni=dni, apellido=ape, nombre=nom,estado=es, foto=fot)    
#     return JsonResponse({
#         'estado': True,
#         'mensaje': 'Director registrado exitosamente.'
#     })
@csrf_exempt
def guardarDirector(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        dni = request.POST.get("dni")
        apellido = request.POST.get("apellido")
        nombre = request.POST.get("nombre")
        estado = request.POST.get("estado", False) == 'on'  # Convertir a booleano
        foto = request.FILES.get("foto")

        try:
            # Crear una nueva instancia de Director
            nuevoDirector = Director.objects.create(
                dni=dni,
                apellido=apellido,
                nombre=nombre,
                estado=estado,
                foto=foto
            )

            return JsonResponse({
                'estado': True,
                'mensaje': 'Director registrado exitosamente.'
            })
        except Exception as e:
            # Manejar cualquier excepción que pueda ocurrir durante la creación
            return JsonResponse({
                'estado': False,
                'mensaje': f'Error al registrar el director: {str(e)}'
            })
    else:
        # Si no es una solicitud POST, retornar un error
        return JsonResponse({
            'estado': False,
            'mensaje': 'Método no permitido.'
        })

#CON AJAX
def listadoDirectores(request):
    directoresBdd = Director.objects.all()
    return render(request, "listadoDirectores.html", {'directores': directoresBdd})