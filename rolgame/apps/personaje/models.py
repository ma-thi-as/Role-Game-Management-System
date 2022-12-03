from urllib import request
from django.db import models
from apps.usuario.models import Usuario
from apps.equipamiento.models import  Objeto
from apps.raza.models import  Raza
from apps.ataque.models import AtaqueEspecial


# Create your models here.
class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    estadoCombate = models.CharField('Estado de combate (Congelado,etc)',max_length=30,default="Normal",blank=True,null=True)
    descripcion = models.TextField('Descripcion Estado', max_length=200,null=True,blank=True)
    estado = models.BooleanField('Inventario en uso', default=False)

    def __str__(self):
        return f'{self.estadoCombate}'
    



class Personaje(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, default=None)
    raza = models.ForeignKey(Raza, on_delete= models.CASCADE)
    estado_combate = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True, default=None)
    estado = models.BooleanField('Vivo ',default=True,blank=False,null=False)
    nivel = models.PositiveIntegerField(default=1)
    nombrePersonaje = models.CharField('Nombre del personaje', max_length=30,null=False,blank=False, unique=True)
    capcaidad_invetario = (
        (1,1),
        (2,4),
        (3,8),
        (4,10)
    )
    capcaidad_habilidades = (
        (1,2),
        (2,4),
        (3,8)
    )
    capcaidad_poderes = (
        (1,1),
        (2,4),
        (3,6),

    )
    
    capacidad = models.PositiveIntegerField('Capacidad de inventario', choices=capcaidad_invetario, null=False, blank=False)
    habilidades = models.PositiveIntegerField('Capacidad de habilidades',choices=capcaidad_habilidades,null=False,blank=False)
    poderes = models.PositiveIntegerField('Capacidad de poderes',choices=capcaidad_poderes,null=False,blank=False)

    class Meta:
        verbose_name = "Personaje"
        verbose_name_plural = "Personajes"
        ordering = ['usuario']



    def __str__(self):
        return f'{self.nombrePersonaje}'

    def nombre_real_jugador(self):
        return f'{self.usuario.nombre} {self.usuario.apellido}'

    def nombre_equipo(self):
        return f'{self.equipo.objeto_key}'
    
        
    

class Inventario(models.Model):
    id = models.AutoField(primary_key=True)
    personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE, verbose_name="Personaje")
    objeto = models.ForeignKey(Objeto, on_delete=models.PROTECT, verbose_name="Nombre objeto")
    cantidad = models.PositiveIntegerField('Cantidad de objetos',default=1)
    estado = models.BooleanField('En uso', default=True)

    class Meta:
        verbose_name = "Inventario Objeto"
        verbose_name_plural = "Inventario Objetos"
        ordering = ['objeto__nombre']

        
    
    def __str__(self):
        return f' invetario de {self.personaje}'

    def nombre_objeto(self):
        return f'{self.objeto.nombre}'

        

class InventarioAtaque(models.Model):
    id = models.AutoField(primary_key=True)
    personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE, verbose_name="Personaje")
    ataque = models.ForeignKey(AtaqueEspecial, on_delete= models.PROTECT, verbose_name="Ataque especial")
    estado = models.BooleanField('Inventario en uso', default=True)

    class Meta:
        verbose_name = "Inventario Ataque"
        verbose_name_plural = "Inventario Ataques"
        ordering = ['personaje']

        

    def __str__(self):
        return f' Ataque especial de {self.personaje}'

    def daño(self):return f'{self.ataque.daño_fisico}'
    def daño_magico(self):return f'{self.ataque.daño_magico}'
    def ataque_de_raza(self):return f'{self.ataque.raza.nombre}'
