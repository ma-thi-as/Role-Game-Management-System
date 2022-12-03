from django import forms
from .models import Estado, Personaje

class PersonajeForm(forms.ModelForm):
    class Meta:
        model = Personaje
        fields = ['raza','nombrePersonaje','capacidad','habilidades','poderes']
        labels = {
            'raza':'Raza del personaje',
            'nombrePersonaje':'Nombre del personaje',
            'capacidad':'Capacidad de invetario del personaje',
            'habilidades':'Capacidad de habilidades del personaje',
            'poderes':'Capacidad de poderes del personaje',
        }
        widgets = {
            'nombrePersonaje':forms.TextInput(
                attrs ={
                    'class':'form-control'
                }

            )
        }


class PersonajeUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Personaje
        fields = ['estado_combate','nivel']
        labels = {
            'estado_combate':'Estado del personaje en combate',
            'nivel':'Nivel del personaje',

        }
        widgets = {
            'nivel':forms.NumberInput(
                attrs ={
                    'class':'form-control'
                }
            ),'estado_combate':forms.Select(
                attrs ={
                    'class':'form-control'
                }
            )
        }



class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['estadoCombate','descripcion','estado']
        labels = {
            'estadoCombate':'Estado de combate para un personaje',
            'descripcion':'Descripcion del estado para el personaje',
            'estado':'Estado activo',
        }
        widgets = {
            'estadoCombate':forms.TextInput(
                attrs ={
                    'class':'form-control'
                }

            ),'descripcion':forms.Textarea(
                attrs ={
                    'class':'form-control'
                }

            )
        }
