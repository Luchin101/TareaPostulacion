from django.db import models

# Create your models here.
class Curso(models.Model):
	nombre =  models.CharField(max_length=10)

	def __str__(self):
		return self.nombre

class Alumno(models.Model):
	nombre = models.CharField(max_length=70)
	def __str__(self):
		return self.nombre

class GestionCurso(models.Model):
	alumno = models.ForeignKey(Alumno, null=False, blank=False, on_delete=models.CASCADE)
	curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)

	