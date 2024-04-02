from django.shortcuts import render
from AppCoder.models import Curso, Alumno, Profesor
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import *
# Create your views here.

def inicio(request):
    return render(request,"padre.html")

#def alta_curso (request,nombre):
#    curso=Curso(nombre=nombre,camada=4567)
#    curso.save()
#    texto= f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
#    return HttpResponse(texto)


def ver_cursos(request):
    cursos=Curso.objects.all()
    dicc={"cursos":cursos}
    plantilla = loader.get_template("cursos.html")
    documento=plantilla.render(dicc)
    return HttpResponse(documento)

def alumnos(request):
    return render(request, "alumnos.html")

def curso_form(request):   
    if request.method == "POST":
     
     mi_formulario=Curso_formulario(request.POST)
     if mi_formulario.is_valid():       
        datos=mi_formulario.cleaned_data   # Es un diccionario con datos de form limpios, par no tomar datos del request
        curso=Curso(nombre=datos["nombre"], camada=datos["camada"])
        curso.save()
        #texto= f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
        #return HttpResponse(texto)
        return render(request,"registro_ok.html", {"curso":curso})

    return render(request,"formulario.html")

def buscar_curso(request):
   return render (request, "buscar_curso.html")

def buscar(request):
   if request.GET["nombre"]:
      nombre=request.GET["nombre"]
      cursos= Curso.objects.filter(nombre__icontains=nombre)
      return  render(request, "resultado_busqueda.html", {"cursos":cursos})
   else:
      return HttpResponse("Ingrese el nombre del curso")
   
#views de alumnos
def ver_alumnos(request):
    alumnos=Alumno.objects.all()
    dicc={"alumnos":alumnos}
    plantilla = loader.get_template("alumno_alumnos.html")
    documento=plantilla.render(dicc)
    return HttpResponse(documento)

def agregar_alumno(request):
    if request.method == "POST":
     
     mi_formulario=Alumno_formulario(request.POST)  
     if mi_formulario.is_valid():       
        datos=mi_formulario.cleaned_data   # Es un diccionario con datos de form limpios, para no tomar datos de request
        alumno=Alumno(nombre=datos["nombre"], grupo=datos["grupo"],dni=datos["dni"])
        alumno.save()
        #texto= f"Se guardo en la BD el alumno: {alumno.nombre} con DNI {alumno.dni} en el grupo {alumno.grupo}"
        #return HttpResponse(texto)
        return render(request,"alumno_registro_ok.html", {"alumno":alumno})

    return render(request,"alumno_form.html")

def buscar_alumno(request):
   return render (request, "buscar_alumno.html")

def buscar_a(request):
   if request.GET["nombre"]:
      nombre=request.GET["nombre"]
      alumnos= Alumno.objects.filter(nombre__icontains=nombre)
      return  render(request, "alumno_resultado_busqueda.html", {"alumnos":alumnos})
   else:
      return HttpResponse("Ingrese el nombre del alumno")
   
#views de profesores
def ver_profesores(request):
    profesores=Profesor.objects.all()
    dicc={"profesores":profesores}
    plantilla = loader.get_template("profesor_profesores.html")
    documento=plantilla.render(dicc)
    return HttpResponse(documento)

def agregar_profesor(request):
    if request.method == "POST":
     
     mi_formulario=Profesor_formulario(request.POST)  
     if mi_formulario.is_valid():       
        datos=mi_formulario.cleaned_data   # Es un diccionario con datos de form limpios, para no tomar datos de request
        profesor=Profesor(nombre=datos["nombre"], grupo=datos["grupo"],dni=datos["dni"])
        profesor.save()
        return render(request,"profesor_registro_ok.html", {"profesor":profesor})

    return render(request,"profesor_form.html")

def buscar_profesor(request):
   return render (request, "buscar_profesor.html")

def buscar_p(request):
   if request.GET["nombre"]:
      nombre=request.GET["nombre"]
      profesores= Profesor.objects.filter(nombre__icontains=nombre)
      return  render(request, "profesor_resultado_busqueda.html", {"profesores":profesores})
   else:
      return HttpResponse("Ingrese el nombre del profesor")
