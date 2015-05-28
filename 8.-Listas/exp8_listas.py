#!/usr/bin/python
# -*- coding: utf-8 -*-
# AUTOR: Coordinación de Fundamentos de Computación y Programación
# FECHA: Segundo Semestre de 2013
#
# Programa que recibe un número natural n, como entrada de un usuario a partir 
# de éste se crea una lista con todos los números de 1 a n, eleva cada uno de 
# los elementos al cubo, los invierte y los muestra por pantalla al usuario

#
# FUNCIONES
#

    # IMPORTACIÓN DE FUNCIONES
# Desde el módulo math importo la función para elevar al cubo
# from math import pow (?)


    # DEFINICIÓN DE FUNCIONES

# Función que crea una lista con los elementos de uno a un número natural dado
# Entrada: El valor límite de la lista
# Salida: Una lista desde 1 hasta 'n'. Ambos incluidos
def crearLista(n):
    return range(1,n+1)

# Función que eleva al cubo cada elemento de una lista
# Entrada: Una lista de numeros
# Salida: Una nueva lista con todos los elementos de la primera, pero elevados 
# al cubo
def elevarAlCubo(lista):
    result = []

    for num in lista:
        elem = pow(num,3)    # se eleva el numero al cubo
        result.append(elem)  # se agrega el elemento a la lista

    return result

# Función que invierte los elementos de una lista
# Entrada: Una lista cualquiera.
# Salida: Una copia de la lista original, pero invertida.
def invertirLista(lista):
    result = []
    i = -1

    while i >= -len(lista):
        elem = lista[i]
        result.append(elem)
        i -= 1

    return result


# Función que imprime los elementos de una lista en una sola línea
# Entrada: Lista de numeros
# Salida: Nada. Imprime la lista de numeros separados por coma
def imprimirLista(lista):
    text = "%d" % lista[0]

    for elem in lista[1:]:
        text += ", %d" % elem

    print text


# BLOQUE PRINCIPAL
#
    # ENTRADA DE DATOS
# Se solicita el ingreso de n y se valida que sea un número
# natural, en caso de que no sea se pregunta nuevamente

n = -1

while n < 0:
    n = input("Ingrese un número natural: ")

    # PROCESAMIENTO
# Se crea la lista, posteriormente se eleva cada uno de los elementos al
# cubo para finalmente invertir el orden de los elementos de la lista
lista = crearLista(n)

elevarAlCubo(lista)
invertirLista(lista)

    # SALIDA
# Se imprime la salida al usuario
imprimirLista(lista)



# FIN
