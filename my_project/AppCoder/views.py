from django.shortcuts import render
from AppCoder.models import Curso, Alumno, Profesor, Avatar
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

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
    avatares=Avatar.objects.filter(user=request.user.id)
    return render(request, "alumnos.html",{ "url":avatares[0].imagen.url})

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

def eliminar_curso(request, id):
   curso=Curso.objects.get(id=id) #obtener curso por id
   curso.delete()
   curso=Curso.objects.all()
   return render(request,"cursos.html",{"cursos":curso}) # Este paso es para no hacer F5

def editar_curso(request,id):
   curso=Curso.objects.get(id=id)
   if request.method =="POST": #Comportamiento cuando es POST
      mi_formulario =Curso_formulario(request.POST)  #Con los datos de la petición POST genera el formulario 'Curso formulario'
      if mi_formulario.is_valid():
         datos=mi_formulario.cleaned_data
         curso.nombre=datos["nombre"]
         curso.camada=datos["camada"]
         curso.save()
         curso=Curso.objects.all()
         return render(request,"cursos.html",{"cursos":curso}) # Este paso es para no hacer F5

   else: #comportmiento cuando es GET
      mi_formulario=Curso_formulario(initial = {"nombre": curso.nombre, "camada": curso.camada})
      return render(request, "editar_curso.html" , {"mi_formulario":mi_formulario, "curso":curso})

def login_request(request):
   if request.method=="POST":
      form =AuthenticationForm(request, data=request.POST)
      if form.is_valid():
         usuario=form.cleaned_data.get("username")
         contra=form.cleaned_data.get("password")
         user=authenticate(username=usuario, password=contra) #checa si usuario ya existe
         if user is not None:
            login(request,user)
            avatares=Avatar.objects.filter(user=request.user.id)
            return render(request, 'inicio.html', { "url":avatares[0].imagen.url,"mensaje":f"Bienvenido/a {usuario}","usuario":usuario})
         else:
            return HttpResponse(f"Usuario no encontrado")
      else:
         return HttpResponse(f"FORM INCORRECTO {form}")
         
   else:      
      form=AuthenticationForm()
      return render (request, "login.html", {"form":form})

def register(request):
   if request.method =="POST":
      form=UserCreationForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponse("Usuario creado")
   else:
      form=UserCreationForm()
      return render(request, "registro.html", {"form":form})

def editarPerfil(request):
   usuario=request.user
   if request.method=="POST":
      mi_formulario=UserEditForm(request.POST)
      if mi_formulario.is_valid():
         informacion=mi_formulario.cleaned_data
         usuario.email = informacion["email"]
         password=informacion["password1"]
         usuario.set_password(password)
         usuario.save()
         return render (request, "inicio.html")
   else:
      miFormulario=UserEditForm(initial={'email':usuario.email})
   
   return render( request, "editar_perfil.html", {"miFormulario":miFormulario,"usuario":usuario})
   



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
   
def eliminar_alumno(request, id):
   alumno=Alumno.objects.get(id=id) #obtener curso por id
   alumno.delete()
   alumno=Alumno.objects.all()
   return render(request,"alumno_alumnos.html",{"alumnos":alumno})

def editar_alumno(request,id):
   alumno=Alumno.objects.get(id=id)
   if request.method =="POST": #Comportamiento cuando es POST
      mi_formulario =Alumno_formulario(request.POST)  #Con los datos de la petición POST genera el formulario 'Curso formulario'
      if mi_formulario.is_valid():
         datos=mi_formulario.cleaned_data
         alumno.nombre=datos["nombre"]
         alumno.dni=datos["dni"]
         alumno.grupo=datos["grupo"]
         alumno.save()
         alumno=Alumno.objects.all()
         return render(request,"alumno_alumnos.html",{"alumnos":alumno}) # Este paso es para no hacer F5

   else: #comportmiento cuando es GET
      mi_formulario=Alumno_formulario(initial = {"nombre": alumno.nombre, "dni": alumno.dni, "grupo":alumno.grupo})
      return render(request, "editar_alumno.html" , {"mi_formulario":mi_formulario, "alumno":alumno})


   


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

def eliminar_profesor(request, id):
   profesor=Profesor.objects.get(id=id) #obtener curso por id
   profesor.delete()
   profesor=Profesor.objects.all()
   return render(request,"profesor_profesores.html",{"profesores":profesor})

def editar_profesor(request,id):
   profesor=Profesor.objects.get(id=id)
   if request.method =="POST": #Comportamiento cuando es POST
      mi_formulario =Profesor_formulario(request.POST)  #Con los datos de la petición POST genera el formulario 'Curso formulario'
      if mi_formulario.is_valid():
         datos=mi_formulario.cleaned_data
         profesor.nombre=datos["nombre"]
         profesor.dni=datos["dni"]
         profesor.grupo=datos["grupo"]
         profesor.save()
         profesor=Profesor.objects.all()
         return render(request,"profesor_profesores.html",{"profesores":profesor}) # Este paso es para no hacer F5

   else: #comportmiento cuando es GET
      mi_formulario=Profesor_formulario(initial = {"nombre": profesor.nombre, "dni": profesor.dni, "grupo": profesor.grupo})
      return render(request, "editar_profesor.html" , {"mi_formulario":mi_formulario, "profesor":profesor})


