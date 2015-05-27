#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

# DEFINICION DE FUNCIONES 

def circuloArea(radio):
    area = float(math.pi * radio**2)
    return area

def circuloPerimetro(radio):
    perimetro = float(2 * math.pi * radio)
    return perimetro

def trianguloRectanguloArea(b, h):
    area = float(b * h / 2)
    return area

def trianguloRectanguloPerimetro(b, h):
    perimetro = float(b + h + math.sqrt(b**2 + h**2))
    return perimetro

def rectanguloArea(b, h):
    area = float(b * h )
    return area

def rectanguloPerimetro(b, h):
    perimetro = float(2 * (b + h))
    return perimetro

def cuadradoArea(a):
    area = float(a**2)
    return area

def cuadradoPerimetro(a):
    perimetro = float(4 * a)
    return perimetro

# MENU

menu = '''
MENU:
========
Opcion 1: Área y perímetro de un círculo
Opción 2: Área y perímetro de un triángulo rectángulo
Opción 3: Área y perímetro de un rectángulo
Opción 4: Área y perímetro de un cuadrado
'''


print menu

opcion = input("\nElija una opcion: ")
area = 0
perimetro = 0 

if opcion == 1:
    radio = input("\nRadio del circulo: ")
    area = circuloArea(radio)
    perimetro = circuloPerimetro(radio)

elif opcion == 2:
    base = input("\nBase del triangulo: ")
    altura = input("\nAltura del triangulo: ")
    area = trianguloRectanguloArea(base, altura)
    perimetro = trianguloRectanguloPerimetro(base, altura)

elif opcion == 3:
    base = input("\nBase del rectángulo: ")
    altura = input("\nAltura del rectángulo: ")
    area = rectanguloArea(base, altura)
    perimetro = rectanguloPerimetro(base, altura)

elif opcion == 4:
    lado = input("\nLado del cuadrado: ")
    area = cuadradoArea(lado)
    perimetro = cuadradoPerimetro(lado)

else:
    print "Opcion «%d» no definida" % opcion
    exit(1)

print "Area: %.2f " % (area)
print "Perimetro: %.2f " % (perimetro)

