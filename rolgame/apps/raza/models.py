from django.db import models

# Create your models here.

            
class Raza(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la raza',max_length=50, blank=False, null= False)
    descripcion = models.TextField('Detalle de la raza',max_length=200, blank=False, null= False)
    imagen = models.ImageField('Imagen de la raza', upload_to='raza/', height_field=None, width_field=None,null=True,blank=True, max_length=200 )
    estado = models.BooleanField('Raza activa',default= False)

    #Estadistas base
    dañoFisico = models.IntegerField('Daño fisico base', default=10)
    dañoMagico = models.IntegerField('Daño magico base', default=10)
    resistFisica = models.IntegerField('Armadura fisica', default=10)
    resistMagica = models.IntegerField('Armadura magica', default=10)

    class Meta:
        verbose_name = 'raza'
        verbose_name_plural = 'Razas'
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre}'


