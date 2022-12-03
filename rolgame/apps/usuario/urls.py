from django.urls import path
from apps.usuario.views import (
    UsuariosView,
    ListadoUsuario, RegistrarUsuario,UsuarioUpdateView
)

urlpatterns = [
    path('',UsuariosView.as_view(), name='usuarios'),   
    path('registrar_usuario/',RegistrarUsuario.as_view(), name = 'registrar_usuario'),
    path('listar_usuarios/',ListadoUsuario.as_view(), name = 'listar_usuarios'),
    path('editar_usuarios/<int:pk>',UsuarioUpdateView.as_view(), name = 'editar_usuario'),
]