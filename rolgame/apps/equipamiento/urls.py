from django.urls import path
from apps.equipamiento.views import (
    EquipamientoView, EquipamientoCreateView, 
    EquipamientoListView,EquipamientoDeleteView,
    EquipamientoActivoView,EquipamientoUpdateView, InventarioAtaqueCreateView,
    
    InventarioView,InventarioListView,
    InventarioCreateView,InventarioUpdateView,

    InventarioAtaqueView,InventarioAtaqueListView,
    InventarioCreateView,InventarioAtaqueDeleteView)

urlpatterns = [
    path('',EquipamientoView.as_view(),name='equipamiento'),
    path('crear_equipamiento/',EquipamientoCreateView.as_view(), name='crear_equipamiento'),
    path('listar_equipamiento/',EquipamientoListView.as_view(), name='listar_equipamiento'),
    path('elimiar_equipamiento/<int:pk>',EquipamientoDeleteView.as_view(), name='borrar_equipamiento'),
    path('editar_equipamiento/<int:pk>',EquipamientoUpdateView.as_view(), name='editar_equipamiento'),
    path('activo/',EquipamientoActivoView.as_view(), name='equip_activo'),

#VISTAS DEL INVENTARIO GENERAL DE OBJETOS
    path('inventario/',InventarioView.as_view(),name='inventario'),
    path('crear_inventario/',InventarioCreateView.as_view(), name='crear_inventario'),
    path('listar_inventario/',InventarioListView.as_view(), name='listar_inventario'),
    path('borrar_inventario/<int:pk>',InventarioAtaqueDeleteView.as_view(), name='borrar_inventario'),
    path('editar_inventario/<int:pk>',InventarioUpdateView.as_view(), name='editar_inventario'),



#VISTAS DEL INVENTARIO DE HABILIDADES Y PODERES
    path('inventario_especial/',InventarioAtaqueView.as_view(),name='inventario_especial'),
    path('crear_inventario_especial/',InventarioAtaqueCreateView.as_view(), name='crear_inventario_especial'),
    path('listar_inventario_especial/',InventarioAtaqueListView.as_view(), name='listar_inventario_especial'),
    path('borrar_inventario_especial/<int:pk>',InventarioAtaqueDeleteView.as_view(), name='borrar_inventario_especial'),

]