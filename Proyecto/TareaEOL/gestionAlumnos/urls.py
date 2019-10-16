from django.urls import path
from .views import lista_alumnos, crear, eliminar, clase

urlpatterns = [
	path('', clase, name='clase'),
	path('lista_alumnos/<int:id>', lista_alumnos, name='lista_alumnos'),
    path('crear/<int:id>', crear, name='crear'),
    path('eliminar/<int:id>', eliminar, name='eliminar'),
]