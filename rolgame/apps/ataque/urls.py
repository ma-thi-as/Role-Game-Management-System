from django.urls import path
from apps.ataque.views import (
    AtaqueView, AtaqueCreateView,
    AtaqueListView,AtaqueUpdateView,
    AtaqueActivoView,AtaqueDeleteView
)
urlpatterns = [
    #Inicio Ataque page
    path('',AtaqueView.as_view(), name='ataque'),
    path('crear_ataque/',AtaqueCreateView.as_view(), name='crear_ataque'),
    path('listar_ataques/',AtaqueListView.as_view(), name='listar_ataques'),
    path('editar_ataque/<int:pk>',AtaqueUpdateView.as_view(), name='editar_ataque'),
    path('borrar_ataque/<int:pk>',AtaqueDeleteView.as_view(), name= 'borrar_ataque'),
    path('ataque_activo/',AtaqueActivoView.as_view(), name="ataque_activo"),



]