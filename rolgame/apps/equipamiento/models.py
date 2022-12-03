from django.db import models

# Create your models here.


class Objeto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre objeto',max_length=30, null=False , blank=False, unique=True)
    posision_choice =(
        (1,'CASCO'),
        (2,'PECHERA'),
        (3,'GREVAS'),
        (4,'BOTAS'),
        (5,'ARMA PRINCIPAL'),
        (6,'ARMA SECUNDARIA'),
        (7,'POCION DE VIDA '),
        (8,'POCION DE MANA '),
        (9,'MONEDA '),

    )
    categoria_choice={
        (1,'NINGUNA'),
        (2,'ESPADA'),
        (3,'BASTON'),
        (4,'ARCO'),
        (5,'PLATA'),
        (6,'ORO'),

        
    }
    
    posicion = models.PositiveSmallIntegerField('Posicion del objeto', choices=posision_choice)
    categoria = models.PositiveSmallIntegerField('Categoria del objeto', choices=categoria_choice, null=True, blank=True)
    armaduraF = models.IntegerField('Recistencia fisica',null=True, blank=True , default=0)
    armaduraM = models.IntegerField('Recistencia Magica',null=True, blank=True, default=0)
    dañoF = models.IntegerField('Daño fisico',null=True, blank=True, default=0)
    dañoM = models.IntegerField('Daño magico',null=True, blank=True, default=0)
    imagen = models.ImageField('Imagen del objeto', upload_to='Objetos/', height_field=None, width_field=None,null=True,blank=True, max_length=200 )
    estado = models.BooleanField('Inventario en uso', default=False)


    class Meta:
        verbose_name= 'Objeto'
        verbose_name_plural = 'Objetos' 
        ordering = ['nombre']


    
    def __str__(self):
        return f'{self.nombre}'



    