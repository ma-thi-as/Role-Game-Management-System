from django.db import models


from apps.raza.models import Raza
from apps.usuario.models import Usuario

# Create your models here.

class AtaqueEspecial(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre del poder o habilidad',max_length=50, blank=False, null=False, unique=True)
    descripcion = models.TextField('Detalle del poder o habilidad',max_length=200,blank=False,null=False)
    imagen = models.ImageField('Imagen poder', upload_to='Poderes/', height_field = None, width_field=None,null=True,blank=True, max_length=200 )
    daño_fisico = models.IntegerField('Daño fisico', default=10)
    daño_magico = models.IntegerField('Daño magio', default=10)     
    raza = models.ForeignKey(Raza, on_delete= models.PROTECT)
    categoria_choice =(
        (1,'HABILIDAD'),
        (2,'PODER'),
    )
    categoria = models.PositiveIntegerField('Categoria del ataque especial', choices=categoria_choice,blank=False,null=False)
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, null= True, blank=True)
    estado = models.BooleanField('Inventario en uso', default=False)
    
    class Meta:
        verbose_name= 'Ataque especial'
        verbose_name_plural = 'Ataques especiales' 
        ordering = ['nombre']

    def __str__(self) :
        return f'{self.nombre}'

    def devolver(self):
        return dict(AtaqueEspecial.categoria_choice)[self.categoria]