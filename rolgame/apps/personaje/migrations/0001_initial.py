# Generated by Django 4.0.5 on 2022-07-18 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('raza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estadoCombate', models.CharField(blank=True, default='Normal', max_length=30, null=True, verbose_name='Estado de combate (Congelado,etc)')),
                ('descripcion', models.TextField(blank=True, max_length=200, null=True, verbose_name='Descripcion Estado')),
                ('estado', models.BooleanField(default=False, verbose_name='Inventario en uso')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.PositiveIntegerField(default=1, verbose_name='Cantidad de objetos')),
                ('estado', models.BooleanField(default=True, verbose_name='En uso')),
            ],
            options={
                'verbose_name': 'Inventario Objeto',
                'verbose_name_plural': 'Inventario Objetos',
                'ordering': ['objeto__nombre'],
            },
        ),
        migrations.CreateModel(
            name='InventarioAtaque',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Inventario en uso')),
            ],
            options={
                'verbose_name': 'Inventario Ataque',
                'verbose_name_plural': 'Inventario Ataques',
                'ordering': ['personaje'],
            },
        ),
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Vivo ')),
                ('nivel', models.PositiveIntegerField(default=1)),
                ('nombrePersonaje', models.CharField(max_length=30, unique=True, verbose_name='Nombre del personaje')),
                ('capacidad', models.PositiveIntegerField(choices=[(1, 1), (2, 4), (3, 8), (4, 10)], verbose_name='Capacidad de inventario')),
                ('habilidades', models.PositiveIntegerField(choices=[(1, 2), (2, 4), (3, 8)], verbose_name='Capacidad de habilidades')),
                ('poderes', models.PositiveIntegerField(choices=[(1, 1), (2, 4), (3, 6)], verbose_name='Capacidad de poderes')),
                ('estado_combate', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='personaje.estado')),
                ('raza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raza.raza')),
            ],
            options={
                'verbose_name': 'Personaje',
                'verbose_name_plural': 'Personajes',
                'ordering': ['usuario'],
            },
        ),
    ]
