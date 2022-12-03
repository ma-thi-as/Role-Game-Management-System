import os , time, django , random as rd
from sqlite3 import Time
from random import random


os.environ.setdefault("DJANGO_SETTINGS_MODULE","rolgame.configuracion.local")

django.setup()

from apps.raza.models import Raza
from apps.equipamiento.models import Categoria


vocales = ['a','e','i','o','u','A','E','I','O','U']
consonantes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','w','x','y','z',
'B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','W','X','Y','Z']


def generate_string(length):
    if length <= 0:
        return False
    
    random_string = ''

    for i in range(length):
        desicion = rd.choice(('vocales','consonantes'))

        if random_string[-1:].lower() in vocales:
            desicion = 'consonantes'
            
        if random_string[-1:].lower() in consonantes:
            desicion = 'vocales'

        if desicion == 'vocales':
            character = rd.choice(vocales)
        else:
            character = rd.choice(consonantes)
        random_string += character

    return random_string

def generate_number():
    return int(random()*10+1)

def generate_raza(count):
    for r in range(count):
            
        random_name = generate_string(generate_number())
        random_descripcion = generate_string(generate_number())

        Raza.objects.create(
            nombre = random_name ,
            descripcion = random_descripcion
        )

def generate_categoria(count):
    for e in range(count):
        random_categoria = generate_string(generate_number())

        Categoria.objects.create(
            categoria = random_categoria
        )

if __name__ == '__main__':
    print("Inicio creacion de objetos")
    print("Porfavor espere ...")
    start = time.strftime("%c")
    print(f"Fecha y hora inicio {start}")
    #Generar objetos 
    generate_categoria(2)

    #
    end = time.strftime("%c")
    print(f"Fecha y hora finalizacion {end}")



            
