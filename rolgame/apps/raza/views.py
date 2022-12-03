from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView,DeleteView, TemplateView


from apps.raza.forms import RazaForm, RazaUpdateForm
from apps.usuario.mixins import LoginStaffMixin
from .models import Raza
# Create your views here.

class tet(TemplateView):
    template_name = 'landingPage/inicio.html'


class RazaView(TemplateView):
    template_name = "razas/raza.html"

class RazaActivaView(LoginStaffMixin,TemplateView):
    template_name = "components/estado_activo.html"


class RazaCreateView(LoginStaffMixin,CreateView):
    model = Raza
    form_class = RazaForm
    template_name = "razas/opciones/crear_raza.html"
    success_url = reverse_lazy('razas:listar_raza')




class ListarRaza(LoginStaffMixin,ListView):
    model = Raza
    template_name = "razas/opciones/listar_razas.html"
    paginate_by = 5
    def get_queryset(self):
        objeto = self.model.objects.all()

        if self.model.objects.filter(estado = False):
            return objeto
        else:
            return objeto


class RazaUpdateView(LoginStaffMixin,UpdateView):
    model = Raza
    form_class = RazaUpdateForm
    template_name = "razas/opciones/crear_raza.html"
    success_url = reverse_lazy('razas:listar_raza')



class RazaDeleteView(LoginStaffMixin,DeleteView):
    model = Raza
    template_name = 'razas/opciones/raza_confirm_delete.html'
    success_url = reverse_lazy ('razas:listar_raza')
    
    def post(self, request, pk,*args, **kwargs):
        object = Raza.objects.get(id=pk)

        if object.estado == True:
            return redirect('razas:raza_activa')

        else:
            object.estado = False
            object.delete()
            return redirect('razas:listar_raza')


        