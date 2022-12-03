from django.contrib import admin
from .models import  Raza
# Register your models here.

class RazaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','descripcion',)
    
admin.site.register(Raza, RazaAdmin)
