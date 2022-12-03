from django.contrib import admin
from django.contrib.auth.models import Permission
from apps.usuario.models import Usuario

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):

    search_fields = ['username']
    list_display = ('username','nombre','apellido','rol')
    
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Permission)

