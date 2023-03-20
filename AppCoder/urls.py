from django.urls import path

from AppCoder.views import *


urlpatterns = [
    path('cursos', cursos, name="AppCoderCursos"),
    path('buscar_cursos', busqueda_curso, name="AppCoderBuscarCurso"),
    path('curso/<nombre>/<camada>', crear_curso, name="AppCoderCurso"),
    path('estudiante/<nombre>/<apellido>/<telefono>/<email>', crear_estudiante, name="AppCoderEstudiantes"),
    path('profesores/<nombre>/<apellido>/<telefono>/<email>/<profesion>', crear_profesor, name="AppCoderProfesores"),
    path('estudiantes', estudiantes, name="AppCoderEstudiantes"),
    path('profesores', profesores, name="AppCoderProfesores"),
    path('busqueda_alumno',busqueda_alumno, name="AppCoderBuscarAlumno"),
    path('busqueda_profesor',busqueda_profesor, name="AppCoderBuscarProfesor")
 ]