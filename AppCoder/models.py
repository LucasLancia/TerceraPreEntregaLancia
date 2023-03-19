from django.db import models

class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    camada=models.IntegerField(max_length=40)

    def __str__(self):
        return f"Curso: {self.nombre}, Comision: {self.camada}"

class Estudiante(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()

    def __str__(self):
        return f"Estudiante: {self.nombre}, Apellido: {self.apellido}, email: {self.email}"

class Profesor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    profesion= models.CharField(max_length=40)

    def __str__(self):
        return f"Profesor: {self.nombre},{self.apellido}"