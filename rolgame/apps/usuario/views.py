#Importaciones de django
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.views.generic import ListView,TemplateView,CreateView,UpdateView
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
#Imporaciones personales
from apps.usuario.mixins import LoginStaffMixin, LoginSuperuserMixin
from .forms import  FormularioLogin, FormularioUsuario, UsuarioUpdateForm
from apps.usuario.models import Usuario 

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"


class UsuariosView(TemplateView):
    template_name = "usuarios/usuarios.html"


class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
    
            return HttpResponseRedirect(self.get_success_url())
        else:

            return super(Login,self).dispatch(request,*args,**kwargs)
        
    def form_valid(self, form):
        login(self.request, form.get_user())
        
        return super(Login,self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/')





class ListadoUsuario( LoginStaffMixin,ListView):
    model = Usuario
    template_name= 'usuarios/opciones/listar_usuarios.html'
    success_url = reverse_lazy('index')
    paginate_by = 5 # PAGINACION


    def get_queryset(self):
        return self.model.objects.filter(is_active = True)


class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name ='usuarios/opciones/crear_usuario.html'
    success_url = reverse_lazy('index')

class UsuarioUpdateView(LoginSuperuserMixin,UpdateView):
    model = Usuario
    template_name = "usuarios/opciones/crear_usuario.html"
    form_class = UsuarioUpdateForm
    success_url = reverse_lazy('usuarios:listar_usuarios')

