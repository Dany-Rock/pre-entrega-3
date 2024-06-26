from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path ("", views.inicio, name="home"),
    path ("ver_cursos", views.ver_cursos, name ="cursos"),
    #path("alta_curso/<nombre>", views.alta_curso),    ingresa curso sin ninguna restriccion
    path("alta_curso", views.curso_form, name="alta_curso"),
    path("alumnos",views.alumnos,name="alumnos"),
    path("buscar_curso",views.buscar_curso, name="buscarcurso"),
    path("buscar", views.buscar),
    path("eliminar_curso/<int:id>", views.eliminar_curso, name="eliminar_curso" ),
    path("editar_curso/<int:id>" , views.editar_curso, name = "editar_curso"),
    path("login",views.login_request, name="Login"), #name es util par type url?
    path("register", views.register, name="Register"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="Logout" ),
    path("editarPerfil", views.editarPerfil, name="EditarPerfil"),



#URL alumnos

    path("ver_alumnos",views.ver_alumnos, name ="ver_alumnos"),
    path("agregar_alumno",views.agregar_alumno, name="alta_alumno"),
    path("buscar_alumno",views.buscar_alumno, name="buscaralumno"),
    path("buscar_a", views.buscar_a),
    path("eliminar_alumno/<int:id>", views.eliminar_alumno, name="eliminar_alumno" ),
    path("editar_alumno/<int:id>" , views.editar_alumno, name = "editar_alumno"),

#URL profesores
    path("ver_profesores",views.ver_profesores, name ="ver_profesores"),
    path("agregar_profesor",views.agregar_profesor, name="alta_profesor"),
    path("buscar_profesor",views.buscar_profesor, name="buscarprofesor"),
    path("buscar_p", views.buscar_p),
    path("eliminar_profesor/<int:id>", views.eliminar_profesor, name="eliminar_profesor" ),
    path("editar_profesor/<int:id>" , views.editar_profesor, name = "editar_profesor"),

]