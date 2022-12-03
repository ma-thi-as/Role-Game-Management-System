from django.urls import path
from apps.personaje.views import (
    PersonajeView,PersonajeCreateView,
    PersonajeListView,PersonajeUpdateView,
    EstadoView,EstadoCreateView,EstadoListView,
    EstadoUpdateView,EstadoDeleteView,EstadoActivoView
    )
urlpatterns = [
    path('',PersonajeView.as_view(), name='personaje'),
    path('crear_personaje/',PersonajeCreateView.as_view(), name='crear_personaje'),
    path('listar_personajes/',PersonajeListView.as_view(), name='listar_personaje'),
    path('editar_personajes/<int:pk>',PersonajeUpdateView.as_view(), name='editar_personaje'),

    path('estado/',EstadoView.as_view(), name='estado'),
    path('activo/',EstadoActivoView.as_view(), name='estado_activo'),
    path('crear_estado/',EstadoCreateView.as_view(), name='crear_estado'),
    path('listar_estados/',EstadoListView.as_view(), name='listar_estado'),
    path('editar_estado/<int:pk>',EstadoUpdateView.as_view(), name='editar_estado'),
    path('borrar_estado/<int:pk>',EstadoDeleteView.as_view(), name='borrar_estado'),

]