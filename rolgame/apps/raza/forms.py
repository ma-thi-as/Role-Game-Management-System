from django import forms
from .models import Raza

class RazaForm(forms.ModelForm):
    class Meta:
        model = Raza
        fields = ['nombre','descripcion','imagen','dañoFisico','dañoMagico','resistFisica','resistMagica']
        labels = {
            'nombre':'Nombre de la raza',
            'descripcion': 'Descripcion de la raza',
            'imagen': 'Imagen de la raza',
            'dañoFisico':'Daño fisico',
            'dañoMagico' :'Daño magico',
            'resistFisica': 'Armadura fisica', 
            'resistMagica': 'Armadura magica' 
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
                    'id':'descripcion',
                }
            ),
            'dañoFisico':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'id':'daño-fisico'

                }
            ),'dañoMagico':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'id':'daño-magico'
                }
            ),'resistFisica':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'id':'resitF'
                }
            ),'resistMagica':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'id':'resitM'

                }
            ),
        }


class RazaUpdateForm(forms.ModelForm):
    class Meta:
        model = Raza
        fields = ['nombre','descripcion','imagen','dañoFisico','dañoMagico','resistFisica','resistMagica','estado']


        labels = {
            'nombre':'Nombre de la raza',
            'imagen': 'Imagen de la raza',
            'dañoFisico':'Daño fisico',
            'dañoMagico' :'Daño magico',
            'resistFisica': 'Armadura fisica', 
            'resistMagica': 'Armadura magica' ,
            'estado':'Raza activa'
        }

        widgets = {
            'nombre': forms.TextInput(
                attrs={

                    'class':'form-control',
                    'placeholder':'Ingrese nombre de la raza...',
                    'id':'nombre'

                }
            ),

            'dañoFisico':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'id':'daño-fisico'

                }
            ),'dañoMagico':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'id':'daño-magico'

                }
            ),'resistFisica':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'id':'resitF'

                }
            ),'resistMagica':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'id':'resitM'

                }
            ),'estado':forms.CheckboxInput()
        }


