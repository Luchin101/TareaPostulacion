from django.contrib import admin
from .models import Curso, Alumno, GestionCurso

# Register your models here.
admin.site.register(Curso)
admin.site.register(Alumno)
admin.site.register(GestionCurso)