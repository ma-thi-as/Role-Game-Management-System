from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,TemplateView,CreateView,UpdateView,DeleteView

from apps.usuario.mixins import LoginMixin, LoginStaffMixin 
from apps.personaje.models import    InventarioAtaque, Inventario, Personaje
from apps.usuario.models import Usuario
from apps.ataque.models import AtaqueEspecial
from apps.raza.models import Raza
from .models import Objeto
from .forms import InventarioForm, ObjetoForm, ObjetoUpdateForm, InventarioAtaqueForm


# Create your views here.

#######VISTAS BASADAS EN CLASE (TEMPLATEVIEW, LISTVIEW, CREATEVIEW, UPDATEVIEW, DELETEVIEW)########

class EquipamientoView(TemplateView):
    template_name = "equipamiento/equipamiento.html"


class EquipamientoActivoView(LoginStaffMixin,TemplateView):
    template_name = "components/estado_activo.html"

class EquipamientoListView(LoginStaffMixin,ListView):
    model = Objeto
    template_name = "equipamiento/opciones/listar_equipamiento.html"
    paginate_by = 5 #SE DEFINE LA PAGINACION COMPLEMENTADA CON BOOSTRAP Y HTML

    def get_queryset(self):
        #REDIFINIR A FALSE
        return self.model.objects.all()


class EquipamientoCreateView(LoginStaffMixin,CreateView):
    model = Objeto
    form_class = ObjetoForm
    template_name = "equipamiento/opciones/crear_equipamiento.html"
    success_url = reverse_lazy('equipamientos:listar_equipamiento')


class EquipamientoListView(LoginStaffMixin,ListView):
    model = Objeto
    template_name = "equipamiento/opciones/listar_equipamiento.html"
    paginate_by = 5

    def get_queryset(self):
        #REDIFINIR A FALSE
        return self.model.objects.all()


class EquipamientoUpdateView(LoginStaffMixin,UpdateView):
    model = Objeto    
    form_class = ObjetoUpdateForm
    template_name = "equipamiento/opciones/crear_equipamiento.html"
    success_url = reverse_lazy('equipamientos:listar_equipamiento')


class EquipamientoDeleteView(LoginStaffMixin,DeleteView):
    model = Objeto
    template_name = 'equipamiento/opciones/equip_confirm_delete.html'
    success_url = reverse_lazy('equipamientos:listar_equipamiento')

    def post(self, request, pk, *args, **kwargs):
        """Redifinicion del metodo post para generar una eliminacion logica dentro de la base de datos, ya que los modelos
        Estan protegidos a la emilinacion ya que estan relacionados en el modelo. 
        """
        object = Objeto.objects.get(id = pk)
        if object.estado == True:
            return redirect('equipamientos:equip_activo')
        else:
            object.estado = False
            object.save()
        return redirect('equipamientos:listar_equipamiento')



class InventarioView(LoginMixin,TemplateView):
    template_name = "equipamiento/inventario/inventario.html"

class InventarioListView(LoginMixin,ListView):
    model = Inventario
    template_name = "equipamiento/inventario/inventario_general/listar_inventario.html"
    paginate_by = 5        

    def get_queryset(self):
        usuario_actual = self.request.user
        consulta_obtener_id  = Usuario.objects.filter(username = usuario_actual).values('id').first()
        obtener_valor = (consulta_obtener_id.get('id'))
        return self.model.objects.filter(personaje__usuario_id = obtener_valor, personaje__estado = True)
            
            
         
        
class InventarioCreateView(LoginMixin,CreateView):
    model = Inventario
    form_class = InventarioForm
    template_name = "equipamiento/inventario/inventario_general/crear_inventario.html"
    success_url = reverse_lazy('equipamientos:listar_inventario')

    def get_form_kwargs(self):
        """Funcionalidad: encargada de obtener argumentos necesarios, a de generar los **kwargs  para hacer una consulta request
        En el formulario InventarioForm.
        """
        kw = super(InventarioCreateView, self).get_form_kwargs()
        kw['request'] = self.request 
        return kw

    def form_valid(self, form) :
        actualizar_estado_objt = Objeto.objects.update(estado = True)
        form.instance.usuario = self.request.user
        form.instance.objeto.estado = actualizar_estado_objt
        
        return super().form_valid(form)


class InventarioDeleteView(DeleteView):
    model = Inventario
    template_name = 'equipamiento/inventario/inventario_general/opciones/inventario_confirm_delete.html'
    success_url = reverse_lazy ('equipamientos:listar_inventario_especial')


class InventarioUpdateView(UpdateView):
    model = Inventario
    fields = ['objeto','cantidad']
    template_name = 'equipamiento/inventario/inventario_general/crear_inventario.html'
    success_url = reverse_lazy('equipamientos:listar_inventario')






class InventarioAtaqueView(LoginMixin,TemplateView):
    template_name = "equipamiento/inventario/ineventario.html"


class InventarioAtaqueListView(LoginMixin,ListView):
    model = InventarioAtaque
    paginate_by = 5  #Paginacion
    
    template_name = "equipamiento/inventario/inventario_ataque/opciones/listar_inventario.html"

    def get_queryset(self):
        usuario_actual = self.request.user
        consulta_obtener_id  = Usuario.objects.filter(username = usuario_actual).values('id').first()
        obtener_valor = (consulta_obtener_id.get('id'))

        return self.model.objects.filter(personaje__usuario_id = obtener_valor, personaje__estado = True)


        
        



class InventarioAtaqueCreateView(LoginMixin,CreateView):
    model = InventarioAtaque
    form_class = InventarioAtaqueForm
    template_name = "equipamiento/inventario/inventario_ataque/opciones/crear_inventario.html"
    success_url = reverse_lazy('equipamientos:listar_inventario_especial')
    
    def get_form_kwargs(self):
        """Funcionalidad: encargada de obtener argumentos necesarios, a de generar los **kwargs  para hacer una consulta request
        En el formulario InventarioForm.
        """
        kw = super(InventarioAtaqueCreateView, self).get_form_kwargs()
        kw['request'] = self.request 
        return kw

    def form_valid(self, form) :
        actualizar_estado_atque = AtaqueEspecial.objects.update(estado = True)
        form.instance.usuario = self.request.user
        form.instance.ataque.estado = actualizar_estado_atque
        return super().form_valid(form)




class InventarioAtaqueDeleteView(DeleteView):
    model = InventarioAtaque
    template_name = 'equipamiento/inventario/inventario_ataque/opciones/ataque_confirm_delete.html'
    success_url = reverse_lazy ('equipamientos:listar_inventario_especial')
