from cProfile import run
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
# Create your models here.


class UsuarioManager(BaseUserManager):
    def _create_user(self,username,email,nombre,password,is_staff,is_superuser,**extra_fields):
        user = self.model(
            username = username,
            email = email,
            nombre = nombre,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self,username,email,nombre,password = None,**extra_fields):
        return self._create_user(username,email,nombre,password,True,False,**extra_fields)

    def create_superuser(self,username,email,nombre,password = None,**extra_fields):
        return self._create_user(username,email,nombre,password,True,True,**extra_fields)



class Usuario(AbstractBaseUser,PermissionsMixin):
    class Types(models.TextChoices):

        GAMEMASTER = 'GAMEMASTER','Gamemaster'
        JUGADOR = 'JUGADOR', 'Jugador'
        

    type = models.CharField(_('Rol'), choices=Types.choices, default=Types.JUGADOR , max_length=30)
    username = models.CharField('Nombre usuario', max_length=30, unique=True)
    email = models.EmailField('Correo electronico', max_length=250, unique= True)
    nombre = models.CharField('Nombre', max_length=30)
    apellido = models.CharField('Apellido', max_length=30)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField('Es miembro del staff',default= False)
    objects = UsuarioManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombre','apellido']


    def __str__(self) :
        return f'{self.username}'
    
    def rol(self):
        return self.type

    def admin(self):
        return self.is_superuser


class GamemasterManager(models.Manager):
    def get_queryset(self,*args, **kwargs):
        return super().get_queryset(*args,**kwargs).filter(type = Usuario.Types.GAMEMASTER)


class Gamemaster(Usuario):
    objects = GamemasterManager()
    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Usuario.Types.GAMEMASTER
        return super().save(*args,**kwargs)

class JugadorManager(models.Manager):
    def get_queryset(self,*args, **kwargs):
        return super().get_queryset(*args,**kwargs).filter(type = Usuario.Types.JUGADOR)


class Jugador(Usuario):
    objects = JugadorManager()
    class Meta:
        proxy = True

    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Usuario.Types.JUGADOR
        return super().save(*args,**kwargs)