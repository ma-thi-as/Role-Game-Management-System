from django.contrib import admin

from apps.ataque.models import AtaqueEspecial

# Register your models here.

class AtaqueEspecialAdmin(admin.ModelAdmin):
    search_fields = ['nombre','categoria','raza']
    list_display = ('nombre','categoria','daño_fisico','daño_magico','raza',)
admin.site.register(AtaqueEspecial,AtaqueEspecialAdmin)
