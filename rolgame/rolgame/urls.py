from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required
from apps.usuario.views import Home, Login, logoutUsuario


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view(),name='index'),
    path('usuarios/login/',Login.as_view(), name='login'),
    path('logout/',login_required(logoutUsuario), name='logout'),
    path('razas/', include(('apps.raza.urls','razas'))),
    path('equipamientos/', include(('apps.equipamiento.urls','equipamientos'))),
    path('ataques/', include(('apps.ataque.urls','ataques'))),
    path('personajes/', include(('apps.personaje.urls','personajes'))),
    path('usuarios/',include(('apps.usuario.urls','usuarios'))),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve,{
        'document_root': settings.MEDIA_ROOT,
    }
)
]