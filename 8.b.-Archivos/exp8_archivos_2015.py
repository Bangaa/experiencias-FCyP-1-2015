#!/usr/bin/python
# -*- coding: utf-8 -*-
#

from random import randint

    # FUNCIONES

# Funcion que genera una matriz de numeros naturales aleatorios
#
# @param n  Numero de filas
# @param m  Numero de columnas
#
# @return Una matriz con numeros naturales aleatorios
def crearMatrizAleatoria(n, m):
    matrix = []

    for i in range(n):
        fila = []   # fila que voy a agregar a la matriz

        for j in range(m):
            num = randint(0, 2**31)

            while num in fila:
                num = randint(0, 2**31)

            fila.append(num)

        matrix.append(fila)

    return matrix

# Escribe una matriz en un archivo
#
# @param matrix     Es la matriz que se escribe
# @param filename   Es el nombre del archivo de salida
#
# @return Nada.
def writeToFile(matrix, filename):

    text = ""

    for fila in matrix:
        for elem in fila:
            text += str(elem) + " "
        text += "\n"
    
    output = open(filename, "w")
    output.write(text)
    output.close() 


# Imprime una lista de listas en forma de matriz
#
# @param matrix Es la matriz que se quiere imprimir
# @return Nada
def printMatrix(matrix):
    for fila in matrix:
        print fila


# Funcion que pide un número natural al usuario
#
# @param prompt Texto que se le muestra al usuario antes de esperar la entrada 
# por teclado.  
#
# @return La entrada que ingresa el usuario que cumple con todas las 
# condiciones
def input_v(prompt):
    inp = -1
    while not esNatural(inp):
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

    # ENTRADA DE DATOS
# Se pide las dimensiones de la matriz (numeros de filas y columnas) al 
# usuario, y se comprueba que la entrada sea correcta

n = input_v("Ingrese numero de filas: ")
m = input_v("Ingrese numero de columnas: ")

    # PROCESAMIENTO
# Se crea la matriz aleatoria con las dimensiones especificadas por el usuario

matriz = crearMatrizAleatoria(n,m)

    # SALIDA
# Se escribe la matriz aleatoria al archivo de salida 'matriz.txt'

writeToFile(matriz, "matriz.txt")
