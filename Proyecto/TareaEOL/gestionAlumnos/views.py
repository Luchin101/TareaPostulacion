from django.shortcuts import render, redirect
#from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from .models import Curso, Alumno, GestionCurso
# Create your views here.

def lista_alumnos(request, id):
	alumnos = GestionCurso.objects.filter(curso__id=id)
	return render(request, 'alumnos.html', {'alumnos':alumnos, 'cursoid':id})

def crear (request, id):
	if request.method == "POST":
		alumno = request.POST.get("nombres","").split('\n')
		curso = Curso.objects.get(id=id)
		for a in alumno:
			estudiante = Alumno()
			estudiante.nombre = a
			estudiante.save()

			gCurso = GestionCurso()
			gCurso.alumno = estudiante
			gCurso.curso = curso
			gCurso.save()

		return redirect('lista_alumnos', id)

	return render(request, 'alumnos-form.html', {'cursoid':id})

def eliminar(request, id):
	if request.method == "POST":
		alumnos = request.POST.getlist('checkbox')
		for a in alumnos:
			alumnoCurso = GestionCurso.objects.get(id=a)
			alumnoCurso.delete()
		return redirect('lista_alumnos', id)

	return redirect('lista_alumnos', id)

def clase(request):
	cursos = Curso.objects.all()
	return render(request, 'cursos.html', {'cursos':cursos})
