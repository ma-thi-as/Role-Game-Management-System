from django.urls import path
from apps.raza.views import(
    RazaView, ListarRaza, 
    RazaCreateView,RazaUpdateView,
    RazaDeleteView, RazaActivaView,
    tet
)

urlpatterns = [
    path('',RazaView.as_view(), name="raza"),
    path('crear_raza/',RazaCreateView.as_view(), name= 'crear_raza'),
    path('listar_razas/',ListarRaza.as_view(), name= 'listar_raza'),
    path('editar_raza/<int:pk>',RazaUpdateView.as_view(), name= 'editar_raza'),
    path('borrar_raza/<int:pk>',RazaDeleteView.as_view(), name= 'borrar_raza'),
    path('listar_razas/',ListarRaza.as_view(), name= 'listar_raza'),
    path('activa/',RazaActivaView.as_view(), name= 'raza_activa'),
    path('tet/',tet.as_view(), name= 'tet'),

]