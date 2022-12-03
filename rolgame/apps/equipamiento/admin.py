from django.contrib import admin

from apps.equipamiento.models import Objeto


class ObjetoAdmin(admin.ModelAdmin):
    search_fields = ['nombre','categoria','posicion']
    list_display = ('nombre','posicion','categoria',)


admin.site.register((Objeto),ObjetoAdmin)
