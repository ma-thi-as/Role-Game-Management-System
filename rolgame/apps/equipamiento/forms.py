from re import T
from django import forms

from apps.ataque.models import AtaqueEspecial


from .models import Objeto
from apps.personaje.models import(
     Inventario, InventarioAtaque, Personaje
     )

class ObjetoForm(forms.ModelForm):
    class Meta:
        model = Objeto
        fields = ['nombre','posicion','categoria','armaduraF','armaduraM','dañoF','dañoM','imagen',]
        labels = {
            'nombre':'Nombre del objeto',
            'posicion':'Posicion en el inventario',
            'categoria':'Categoria del objeto',
            'armaduraF':'Armadura fisica',
            'armaduraM':'Armadura magica',
            'dañoF':'Daño fisico',
            'dañoM' :'Daño magico',
            'imagen':'Imagen del ataque',
        }
        


        widgets = {
             'nombre': forms.TextInput(
                attrs={

                    'class':'form-control',
                    'placeholder':'Ingrese nombre del objeto...',
                    'id':'nombre'

                }
            ),
            
            'armaduraF':forms.NumberInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'armaduraM':forms.NumberInput(
                attrs={
                    'class':'form-control'

                }
            ),
            'dañoF':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'id':'daño-fisico'

                }
            ),
            'dañoM':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'id':'daño-magico'

                }
            ),
        }


class ObjetoUpdateForm(forms.ModelForm):
    class Meta:
        model = Objeto
        fields = ['nombre']
        labels ={
            'nombre':'Nombre del objeto:'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control'

                }
            )
        }

class InventarioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """Constructor que recive los *args, **kwargs("Traidos desde la vista.") 
        Ademas de instanciar al formulario para darle los kwargs para utilizar request y 
        generar la queryset del ORM de Django:

        La cual obtiene exclusivamente los personajes creados por el y con el estado del personaje en vivo(True)
        """
        self.request = kwargs.pop('request')
        super(InventarioForm, self).__init__(*args, **kwargs)
        #Constual al formulario.
        self.fields['personaje'].queryset= Personaje.objects.filter(usuario = self.request.user.id, estado = True)

    class Meta:
        model = Inventario
        fields = ['cantidad','objeto','personaje']
        labels ={
            'cantidad':'Cantidad del objeto',
            'objeto':'Nombre del objeto'
        }
        widgets = {
            'cantidad': forms.NumberInput(
                attrs={
                    'class':'form-control'

                }
            )
        }


class InventarioAtaqueForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """Constructor que recive los *args, **kwargs("Traidos desde la vista.") 
        Ademas de instanciar al formulario para darle los kwargs para utilizar request y 
        generar la queryset del ORM de Django:

        La cual obtiene los usuarios que tengan el mismo id que el creador y con el estado del personaje en vivo(True) """
        self.request = kwargs.pop('request')
        super(InventarioAtaqueForm, self).__init__(*args, **kwargs)
        #Constual al formulario.
        pj_raza_id = Personaje.objects.filter(usuario = self.request.user.id, estado = True, raza__estado = True).values('raza__id')
        excluir_pj = Personaje.objects.exclude(raza__estado = True).values('raza__id')
        self.fields['personaje'].queryset= Personaje.objects.filter(usuario = self.request.user.id, estado = True)
        self.fields['ataque'].queryset = AtaqueEspecial.objects.filter(raza__id__in = pj_raza_id).exclude(raza__id__in = excluir_pj)


    class Meta:
        model = InventarioAtaque
        fields = ['ataque','personaje']
        labels ={
            'cantidad':'Cantidad del objeto',
            'ataque':'Habilidad o poder',

        }
        widgets = {
            'cantidad': forms.NumberInput(
                attrs={
                    'class':'form-control'

                }
            )
        }