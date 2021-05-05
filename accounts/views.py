from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import *

def home(request):
    student=Estudiante.objects.all()
    company=Empresa.objects.all()
    estado=Estado.objects.all() #Ese estado es llamado en (2)
    jobs=Trabajo.objects.all() #el jobs puede ser cualquier nombre pero hay q llamarla abajo, y Trabajo de la tabla de models.py

    total_trabajo= jobs.count()   #aqui y el nombre de total_trabajo puede ser cualquier nombre

    activo=estado.filter(status='Activo').count() #aqui(2)
    pendiente=estado.filter(status='Pendiente').count()


    context={'estudiante':student, 'empresa':company, 'ultimas5':estado, 'totalTrabajo':total_trabajo, 
    'totalActivo':activo, 'totalPendiente':pendiente}
    return render(request,'accounts/inicio.html', context) #pantalla inicio
    
def jobs(request):
    jobs = Trabajo.objects.all()
    context={'trabajo':jobs}
    return render(request,'accounts/trabajo.html', context)

def student(request):
    return render(request,'accounts/estudiante.html')

def company(request):
    return render(request,'accounts/compañia.html')
