from django.urls import path
from . import views

urlpatterns =[
    path ("", views.inicio, name="home"),
    path ("ver_cursos", views.ver_cursos, name ="cursos"),
    #path("alta_curso/<nombre>", views.alta_curso),    ingresa curso sin ninguna restriccion
    path("alta_curso", views.curso_form, name="alta_curso"),
    path("alumnos",views.alumnos,name="alumnos"),
    path("buscar_curso",views.buscar_curso, name="buscarcurso"),
    path("buscar", views.buscar),

#URL alumnos

    path("ver_alumnos",views.ver_alumnos, name ="ver_alumnos"),
    path("agregar_alumno",views.agregar_alumno, name="alta_alumno"),
    path("buscar_alumno",views.buscar_alumno, name="buscaralumno"),
    path("buscar_a", views.buscar_a),

#URL profesores
    path("ver_profesores",views.ver_profesores, name ="ver_profesores"),
    path("agregar_profesor",views.agregar_profesor, name="alta_profesor"),
    path("buscar_profesor",views.buscar_profesor, name="buscarprofesor"),
    path("buscar_p", views.buscar_p),

]