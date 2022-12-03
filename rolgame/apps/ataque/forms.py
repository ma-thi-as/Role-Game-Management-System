from django import forms

from apps.usuario.models import Usuario
from .models import AtaqueEspecial


class AtaqueEspecialForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """Constructor que recive los *args, **kwargs("Traidos desde la vista.") 
        Ademas de instanciar al formulario para darle los kwargs para utilizar request y 
        generar la queryset del ORM de Django:

        La cual obtiene exclusivamente  los personajes creados por el."""
        self.request = kwargs.pop('request')
        super(AtaqueEspecialForm, self).__init__(*args, **kwargs)
        #Constual al formulario.
        self.fields['creador'].queryset= Usuario.objects.filter(id = self.request.user.id)

    class Meta:
        model = AtaqueEspecial
        fields = ['nombre','descripcion','imagen','daño_fisico','daño_magico','categoria','raza','creador']
        labels = {
            'nombre':'Nombre del ataque',
            'descripcion':'Detalle del ataque',
            'imagen':'Imagen del ataque',
            'daño_fisico':'Daño fisico',
            'daño_magico' :'Daño magico',
            'raza':'Raza',
            'categoria':'categoria',
        }

        widgets = {
             'nombre': forms.TextInput(
                attrs={

                    'class':'form-control',
                    'placeholder':'Ingrese nombre de la raza...',
                    'id':'nombre'

                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese descripcion de la raza...',
                    'id':'descripcion'

                }
            ),

            'daño_fisico':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'id':'daño-fisico'

                }
            ),'daño_magico':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'id':'daño-magico'

                }
            ),
        }

class AtaqueUpdateForm(forms.ModelForm):
    
    class Meta:
        model = AtaqueEspecial
        exclude = ['nombre','imagen','daño_fisico','daño_magico','categoria','raza','creador']
        labels = {
            'descripcion':'Detalle del ataque',
            'estado':'Habilidad activa',
        }

        widgets = {
             
            'descripcion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese descripcion de la raza...',
                    'id':'descripcion'

                }
            )
        }