from django.db import models

# Create your models here.

class Estudiante(models.Model):
    name = models.CharField(max_length=200, null=True)
    carrer = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name  #para que muestre el nombre del estuadiante, en la tabla de la base de datos
        #primera base
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name    

class Trabajo(models.Model):
    TYPE =(
            ('Practica','Practica'),
            ('Part-Time','Part-Time'),
            ('Full-Time','Full-Time'),
            )

    name_Job = models.CharField(max_length=200, null=True)
    payment = models.IntegerField(null=True)
    category = models.CharField(max_length=200, null=True,choices=TYPE)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name_Job



class Empresa(models.Model):
    ENTRY = (
            ('Informatica','Informatica'),
            ('Medicina','Medicina'),
            ('Administracion','Administracion'),
            ('Mecanico','Mecanico'),
            ('Otro','Otro'),
            )
    name_company = models.CharField(max_length=200, null=True)
    heading = models.CharField(max_length=200, null=True, choices=ENTRY)
    email = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    date_created = models.DateField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name_company  #para que muestre el nombre del estuadiante, en la tabla de la base de datos
        #tercera base

class Estado(models.Model):
    STATUS = (
            ('Pendiente','Pendiente'),
            ('Fuera de plazo','Fuera de plazo'),
            ('Activo','Activo'),
            )

    estudiante = models.ForeignKey(Estudiante,null=True, on_delete=models.SET_NULL)
    trabajo = models.ForeignKey(Trabajo,null=True, on_delete=models.SET_NULL)
    empresa = models.ForeignKey(Empresa,null=True, on_delete=models.SET_NULL)
    date_created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    
    
    def __str__(self):
        return self.status
    
    #segunda base (Estado, Trabajo)