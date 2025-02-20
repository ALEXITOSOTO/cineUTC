from django.db import models

# Create your models here.
#Crando modelo-tabla Genero: Terror, Comedia, Accion
class Genero(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=25)
    #Por si nos olvidamos de un atributo 
    descripcion=models.CharField(max_length=50, default="") #Se pone default porque en la bdd ya hay datos y no puede agrgar el campo descripcon a ichos datos, por ende es default 
    foto=models.FileField(upload_to='generos',null=True,blank=True)
    #Definir metodo str dentro de la clase Genero para que se muestre mejor
    def __str__(self):
        fila="{0}: {1} - {2}" #Para que se muestre: ID : NOMBRE - DESCRIPCION
        return fila.format(self.id,self.nombre,self.descripcion)

#Crando modelo-tabla Director: Terror, Comedia, Accion
class Director(models.Model):
    id=models.AutoField(primary_key=True)
    dni=models.CharField(max_length=15)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    estado=models.BooleanField(default=True)
    foto=models.FileField(upload_to='directores',null=True,blank=True)

    def __str__(self):
        fila="{0}: {1} - {2} - {3} - {4}"
        return fila.format(self.id,self.dni,self.nombre,self.apellido,self.estado)
    
#Creando modelo-tabla Pais
class Pais(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    continente=models.CharField(max_length=50)
    capital=models.CharField(max_length=50)
    def __str__(self):
        fila="{0}: {1} - {2} - {3}"
        return fila.format(self.id,self.nombre,self.continente,self.capital)
    
class Pelicula(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=250)
    duracion=models.TimeField(null=True)
    sinopsis=models.TextField()
    genero=models.ForeignKey(Genero,on_delete=models.CASCADE)
    director=models.ForeignKey(Director, on_delete=models.CASCADE)
    pais=models.ForeignKey(Pais, on_delete=models.CASCADE)
    portada=models.FileField(upload_to='portadas', null=True, blank=True)

    def __str__(self):
        fila="{0} : {1}"
        return fila.format(self.id,self.titulo)

#Crando modelo-tabla Cine
class Cine(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=250)
    direccion=models.CharField(max_length=250, default='')
    telefono=models.CharField(max_length=250, default='')
    def __str__(self):
        fila="{0} : {1}-{2}"
        return fila.format(self.id,self.nombre,self.direccion)
