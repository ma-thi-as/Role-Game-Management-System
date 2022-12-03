from django import forms
from django.contrib.auth.forms import AuthenticationForm

from apps.usuario.models import Usuario

class FormularioLogin(AuthenticationForm):

    def __init__(self,  *args, **kwargs) :
        super(FormularioLogin,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


class FormularioUsuario(forms.ModelForm):
    password1= forms.CharField(label = 'Contraseña',widget= forms.PasswordInput(
        attrs= {
            'class':'form-control',
            'placeholder':'Ingrese su contraseña...',
            'id':'password1',
            'required':'required',
        }
    ))
    password2= forms.CharField(label = 'Contraseña de confirmacion',widget= forms.PasswordInput(
            attrs= {
                'class':'form-control',
                'placeholder':'Ingrese nuevamente su contraseña...',
                'id':'password2',
                'required':'required',
            }
        ))

    class Meta:
        model = Usuario
        fields = ('email','username','nombre','apellido')
        lables ={
            'email':'Email Usuario',
            'nombre': 'Nombre Usuario',
            'apellido': 'Apellido  Usuario',
            'username':'Username',
        }
        widgets = {
            'email':forms.EmailInput(
                attrs={

                'class':'form-control',
                'placeholder':'Ingrese su correo electronico...',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre...',

                }
            ),
            'apellido':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su apellido...',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre de usuario...',
                }
            )
        }

    def clean_password2(self):
        """
        Validacion de contraseña
        Metodo que valida qye ambas contraseñas sean iguales, antes de ser encriptadas y guardadas en la bd, retorna la contraseña valida
        Exepciones:
        - ValidationError -- cuando las contraseñas no son iguales muestra un mensaje de error
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden!')
        return password2

    def save(self, commit = True):
        user = super().save(commit= False)#Guardamos la instancia de la informacion.
        user.set_password(self.cleaned_data['password1'])
        
        if commit:
            user.save()
        return user


class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        
        fields = ('email','username','nombre','apellido','type','is_staff')
        lables ={
            'email':'Email Usuario',
            'nombre': 'Nombre Usuario',
            'apellido': 'Apellido  Usuario',
            'username':'Username',
            'type':'Tipo de usuario',
            'is_staff':'Privilegios de staff'
        }
        widgets = {
            'email':forms.EmailInput(
                attrs={

                'class':'form-control',
                'placeholder':'Ingrese su correo electronico...',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre...',

                }
            ),
            'apellido':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su apellido...',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre de usuario...',
                }
            ),
            'type': forms.Select(
                attrs={
                    'class':'form-control',
                }
            ),
        }