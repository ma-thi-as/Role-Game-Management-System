from django.contrib import admin

from apps.personaje.models import Estado, InventarioAtaque,  Personaje, Inventario

# Register your models here.

class PersonajeAdmin(admin.ModelAdmin):
    search_fields = ['usuario__nombre','usuario__apellido','nombrePersonaje']
    list_display = ('nombre_real_jugador','nombrePersonaje','estado','nivel','estado_combate','capacidad',)

    
class EstadoAdmin(admin.ModelAdmin):
    search_fields = ['estadoCombate']
    list_display = ('estadoCombate',)

    
class InventarioAdmin(admin.ModelAdmin):
    search_fields = ['personaje']
    list_display = ('personaje','nombre_objeto','cantidad',)

class InventarioAtaqueAdmin(admin.ModelAdmin):
    search_fields = ['personaje']
    list_display = (
        'personaje','ataque','daño','daño_magico','estado',
        'ataque_de_raza',)
    
admin.site.register(Personaje,PersonajeAdmin)
admin.site.register(Estado,EstadoAdmin)
admin.site.register(Inventario,InventarioAdmin)
admin.site.register(InventarioAtaque,InventarioAtaqueAdmin)
