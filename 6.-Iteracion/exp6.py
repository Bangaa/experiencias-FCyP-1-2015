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
# Dice cuantos numeros primos existen entre 2 numeros
#
# @param x  Primer numero
# @param y  Segundo numero
# @return La cantidad de numeros primos entre x e y
def contarPrimosEntre(x, y):
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

# Funcion que pide un número natural al usuario
#
# @param prompt Texto que se le muestra al usuario antes de esperar la entrada 
# por teclado.  
#
# @return La entrada que ingresa el usuario que cumple con todas las 
# condiciones
def input_v(prompt):
    inp = input(prompt)
    while not esNatural(inp):
        print "\nEntrada errónea. Solo números naturales" 
        inp = input(prompt)

    return inp

# Funcion que dice si un numero es natural o no.
# Entrada: Un numero
# Salida: True si el numero es natural, y False en caso contrario
def esNatural(num):
    if num > 0 and int(num) == num:
        return True

    else:
        return False

####################
# BLOQUE PRINCIPAL
####################

inicial = input_v("Dime un numero  : ")
final = input_v("Dime otro numero: ") 

cuantos = contarPrimosEntre(inicial, final)

print "\nhay %d numeros primos entre %d y %d" % (cuantos, inicial, final)
