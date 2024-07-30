from django.db import models

#Creando modelo Género: Terror, Comedia
class Genero (models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=25)
    descripcion=models.CharField(max_length=150, default='')
    foto=models.FileField(upload_to='generos',null=True,blank=True)
    #método
    def __str__(self):
        fila="{0}: {1} - {2}"
        return fila.format(self.id,self.nombre,self.descripcion)
#Creando modelo para Director
class Director (models.Model):
    id=models.AutoField(primary_key=True)
    dni=models.CharField(max_length=15)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    estado=models.BooleanField(default=True)
    foto=models.FileField(upload_to='directores',null=True,blank=True)

    #método 
    def __str__(self):
        fila="{0} : {1}-{2}-{3}"
        return fila.format(self.dni,self.apellido,self.nombre, self.estado)
#Creando modelo para Pais
class Pais (models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=150)
    continente=models.CharField(max_length=150)
    capital=models.CharField(max_length=150)
    def __str__(self):
        fila="{0}: {1} - {2} - {3}"
        return fila.format(self.id,self.nombre,self.continente, self.capital)
#Creando modelo para Película
class Pelicula (models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=250)
    duracion=models.TimeField(null=True) 
    sinopsis=models.TextField()
    genero=models.ForeignKey(Genero, on_delete=models.CASCADE) #PARA AGREGAR UNA CLAVE FORANEA MODELO GENERO
    director=models.ForeignKey(Director, on_delete=models.CASCADE) #PARA AGREGAR UNA CLAVE FORANEA MODELO DIRECTOR
    #portada=models.FileField(upload_to='portadas',null=True,blank=True)
    def __str__(self):
        fila ="{0}: {1}"
        return fila.format(self.id, self.titulo)
#crear modelo CINE    
class Cine(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=25)
    direccion=models.CharField(max_length=150,default='')
    telefono=models.CharField(max_length=150,default='')
    def __str__(self):
        fila="{0}: {1} - {2}"
        return fila.format(self.id,self.nombre,self.direccion)


