#!/usr/bin/python
# -*- coding: utf-8 -*-

##
# Dice si un numero es primo o no
#
# @param num    Es el numero que se verifica
# @return True si es primo; False en caso contrario
def esPrimo(num):
    lim = num
    i = 2
    esprimo = True

    if i > num:
        esprimo = False

    while i < lim and esprimo:
        if num % i == 0:
            esprimo = False
        lim = num/i
        i += 1

    return esprimo

##
# Muestra los numeros primos entre 2 numeros
#
# @param x  Primer numero
# @param y  Segundo numero
# @return La cantidad de numeros primos entre x e y
def entregarPrimosEntre(x, y):
    cuantos = 0
    menor = x if x < y else y
    mayor = y if y > x else x

    print ""
    while menor <= mayor:
        if esPrimo(menor):
            cuantos += 1
            print menor
        menor += 1

    return cuantos

####################
# BLOQUE PRINCIPAL
####################

inicial = input("Dime un numero  : ")
while inicial < 1:
    print "\nEntrada erronea"
    inicial = input("Dime un numero  : ")

final = input("Dime otro numero: ")
while final < 1:
    print "\nEntrada erronea"
    final = input("Dime otro numero: ")


cuantos = entregarPrimosEntre(inicial, final)

print "\nhay %d numeros primos entre %d y %d" % (cuantos, inicial, final)
