from django.shortcuts import render
from app_datos.models import *
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render (request, "padre.html")

# Create your views here.

def registro(request):
    if request.method == "POST":
        ciudadano = Ciudadano(nombre=request.POST["nombre"], edad=request.POST["edad"], ciudad=request.POST["ciudad"])
        ciudadano.save()
        dispositivos = Dispositivos(celular=request.POST["celular"], tablet=request.POST["tablet"], computadora=request.POST["computadora"])
        dispositivos.save()
        tiempo = Tiempo(dias=request.POST["dias"], horas=request.POST["horas"])
        tiempo.save()
        return render(request, "formulario.html")
    return render(request, "formulario.html")



def busqueda_datos(request):
    return render (request, "busqueda_datos.html")



def buscar(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        ciudadano = Ciudadano.objects.filter(nombre__icontains = nombre)
        return render(request, "resultado_busqueda.html", {"ciudadano": ciudadano})  
    else:
        return HttpResponse("Busqueda no tuvo resultados")    
    