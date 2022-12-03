from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import( 
    ListView,TemplateView,
    CreateView,UpdateView,
    DeleteView)

from apps.raza.models import Raza
from apps.personaje.models import Personaje, Estado
from apps.personaje.forms import PersonajeUpdateForm,EstadoForm
from apps.usuario.mixins import LoginMixin,LoginStaffMixin


# Create your views here.



class PersonajeView(LoginMixin,TemplateView):
    template_name = "personajes/personajes.html"



class PersonajeCreateView(LoginMixin,CreateView):
    model = Personaje
    fields = ['raza','nombrePersonaje','capacidad','habilidades','poderes']
    template_name = "personajes/opciones/crear_personajes.html"
    success_url = reverse_lazy('personajes:listar_personaje')

    def form_valid(self, form) :
        actualizar_estado_raza = Raza.objects.update(estado = True)
        
        form.instance.usuario = self.request.user
        form.instance.raza.estado = actualizar_estado_raza
        return super().form_valid(form)


class PersonajeListView(ListView):
    model = Personaje
    template_name = "personajes/opciones/listar_personajes.html"
    paginate_by = 7

    def get_queryset(self):
        if self.request.user.is_staff:
            ###RECORRIDO DE LA CAPACIDAD
            for e in self.model.objects.all():
                if e.capacidad == 1:
                    print("SOLO CAPACIDAD 1")
                elif e.capacidad == 2:
                    print("SOLO CAPACIDAD 2")

            ##############

                    
            
            return self.model.objects.all()


        else: 
            return self.model.objects.filter(usuario= self.request.user)



class PersonajeUpdateView(LoginMixin,UpdateView):
    model = Personaje
    form_class = PersonajeUpdateForm
    template_name = "personajes/opciones/crear_personajes.html"
    success_url = reverse_lazy('personajes:listar_personaje')

    


class EstadoView(LoginStaffMixin,TemplateView):
    template_name = 'personajes/estados/estado.html'

class EstadoActivoView(LoginStaffMixin,TemplateView):
    template_name = "components/estado_activo.html"

class EstadoListView(LoginStaffMixin,ListView):
    model = Estado
    template_name = "personajes/estados/opciones/listar_estado.html"
    paginate_by = 4

    def get_queryset(self):
        return self.model.objects.all()


class EstadoCreateView(LoginStaffMixin,CreateView):
    model = Estado
    form_class = EstadoForm
    template_name = "personajes/estados/opciones/crear_estado.html"
    success_url = reverse_lazy('personajes:listar_estado')



class EstadoUpdateView(LoginStaffMixin,UpdateView):
    model = Estado
    form_class = EstadoForm

    template_name = "personajes/estados/opciones/crear_estado.html"
    success_url = reverse_lazy('personajes:listar_estado')





class EstadoDeleteView(LoginStaffMixin,DeleteView):
    model = Estado
    template_name = "personajes/estados/opciones/estado_confirm_delete.html"

    success_url = reverse_lazy ('personajes:listar_estado')
    
    def post(self, request, pk,*args, **kwargs):
        object = Estado.objects.get( id= pk )

        if object.estado == True:
            return redirect('personajes:estado_activo')

        else:
            object.estado = False
            object.save()
            return redirect('personajes:listar_personaje')


        