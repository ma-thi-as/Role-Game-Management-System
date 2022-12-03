from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView,TemplateView,CreateView,UpdateView, DeleteView

from apps.ataque.forms import AtaqueEspecialForm, AtaqueUpdateForm
from apps.ataque.models import AtaqueEspecial
from apps.usuario.mixins import LoginStaffMixin
from apps.usuario.models import Usuario

# Create your views here.



#VISTAS BASADES EN CLASES

class AtaqueView(TemplateView):
    template_name = "ataques/ataques.html"

class AtaqueActivoView(LoginStaffMixin,TemplateView):
    template_name = "components/estado_activo.html"


class AtaqueCreateView(LoginStaffMixin,CreateView):
    model = AtaqueEspecial
    form_class = AtaqueEspecialForm
    template_name = "ataques/opciones/crear_ataque.html"
    success_url = reverse_lazy('ataques:crear_ataque')

    def get_form_kwargs(self):
            """Funcionalidad: encargada de obtener argumentos necesarios, a de generar los **kwargs  para hacer una consulta request
            En el formulario InventarioForm.
            """
            kw = super(AtaqueCreateView, self).get_form_kwargs()
            kw['request'] = self.request 
            return kw
        



class AtaqueListView(LoginStaffMixin,ListView):
    model = AtaqueEspecial
    template_name = "ataques/opciones/listar_ataque.html"
    paginate_by = 5
    def get_queryset(self):

        usuario_actual = self.request.user
        consulta_obtener_id  = Usuario.objects.filter(username = usuario_actual).values('id').first()
        obtener_valor = (consulta_obtener_id.get('id'))
        t = self.model.objects.filter(estado = False).values('creador')
        print(t)

        return self.model.objects.filter(creador__id = obtener_valor)


class AtaqueUpdateView(LoginStaffMixin,UpdateView):
    model = AtaqueEspecial
    form_class = AtaqueUpdateForm
    template_name = "ataques/opciones/crear_ataque.html"
    success_url = reverse_lazy('ataques:listar_ataques')


class AtaqueDeleteView(LoginStaffMixin,DeleteView):
    model = AtaqueEspecial
    template_name = 'ataques/opciones/ataque_confirm_delete.html'
    success_url = reverse_lazy('ataques:listar_ataques')

    def post(self, request, pk, *args, **kwargs):
        object = AtaqueEspecial.objects.get(id = pk)
        if object.estado == True:
            return redirect('ataques:ataque_activo')

        else:
            object.estado = False
            object.save()

        return redirect('ataques:listar_ataques')


        