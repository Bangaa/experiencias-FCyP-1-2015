#!/usr/bin/python
# -*- coding: utf-8 -*-


##
# Me dice cuantos cigarros puedo hacer dada una cantidad inicial de colillas
# Entrada: Colillas iniciales
# Salida: Cantidad de cigarros que puedo hacer en total, dada la cantidad de 
# colillas iniciales.
def cuantosCigarros(n):
    sobran = n % 5
    cuantos = n/5

    if cuantos > 0:
        cuantos = cuantos + cuantosCigarros(cuantos + sobran)

    return cuantos

##
# Me dice la cantidad de colillas restantes luego de que no pueda hacer mas 
# cigarros. Note que siempre la cantidad de colillas sobrantes es menor que 5, 
# pues si es mayor o igual a 5 entonces puedo hacer un nuevo cigarro.
# Entrada: Cantidad de colillas iniciales
# Salida: Cantidad de colillas sobrantes.
def cuantosSobran(ncolillas):
    sobran = ncolillas % 5
    cigarros = ncolillas / 5

    if cigarros > 0:
        sobran = cuantosSobran(cigarros + sobran)

    return sobran

ncolillas = input("Dígame el numero de colillas: ")

cigarros = cuantosCigarros(ncolillas)
colillas = cuantosSobran(ncolillas)

print "Ud. puede hacer %d cigarros y sobran %d colillas" % (cigarros, colillas)

