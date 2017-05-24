# -*- coding: UTF-8 -*-

# Genere un programa en Python que lea dos matrices de dos archivos de texto 
# (matrizA.txt y matrizB.txt) y con ellas:
#
# - Verifique que tienen dimensiones válidas para ser multiplicadas
# - Realice el cálculo de la multiplicación
# - Escriba el cálculo de la multiplicación en un archivo de texto 
# “resultado.txt”
#
# En caso de que las dimensiones no sean válidas el archivo "resultado.txt" no 
# debe crearse

## IMPORTACIONES

import numpy

## DEFINICION DE FUNCIONES

##
# Lee una matriz desde un archivo de texto. En el archivo, la matriz debe 
# cumplir con el siguiente formato:
# 
#  - cada elemento de una misma fila debe estar separado por un espacio
#  - cada fila debe estar en una linea diferente.
#
# Entrada: el nombre del archivo
# Salida: Un objeto de tipo 'numpy.ndarray' que representa la matriz del 
# archivo.
def leerMatriz(nombreArchivo):
    archivo = open(nombreArchivo, "r")
    matriz = []
    
    for linea in archivo:
        matriz.append(linea.strip().split())

    archivo.close()

    return numpy.array(matriz, dtype='int32')

##
# Indica si el producto interno de matA y matB (en ese orden) es posible.
#
# Entrada: Ambas matrices que se quieren multiplicar. El orden es importante ya 
# que el producto interno no es conmutativo.
#
# Salida: El producto interno de matA y matB
def multiplicables(matA, matB):

    if matA.shape[1] == matB.shape[0]:
        return True

    return False

##
# Escribe la matriz 'numpymat' en el archivo con nombre 'nombreArchivo'.
#
# Entrada numpymat: La matriz que se quiere escribir
# Entrada nombreArchivo: El nombre del archivo de salida.
#
# Salida: Nada.
def escribirMatriz(numpymat, nombreArchivo):

    archivo = open(nombreArchivo, "w")

    archivo.write(ndarrayToStr(numpymat))

    archivo.close()

##
# Da un string que representa el objeto 'numpy.ndarray'. El formato del string 
# cumple con las reglas:
#
#  - cada elemento de una misma fila debe estar separado por un espacio
#  - cada fila debe estar en una linea diferente.
#
# Entrada numpymat: Es el objeto de tipo 'numpy.ndarray' que se quiere 
# representar.
#
# Salida: Un solo string en representacion del array con todos los saltos de 
# linea incluidos.
def ndarrayToStr(numpymat):
    if not type(numpymat) == numpy.ndarray:
        raise TypeError("El argumento de ndarrayToStr() debe ser de tipo 
        numpymat.ndarray no de tipo " + type(numpymat)) 

    matriz = numpymat.tolist()
    strrep = ""

    for fila in matriz:
        strrep += str(fila[0])
        for elem in fila[1:]:
            strrep += " %d" % elem 

        strrep += "\n"

    return strrep

## BLOQUE PRINCIPAL


try:
    a = leerMatriz("matrizA.txt")
    b = leerMatriz("matrizB.txt")
    if multiplicables(a,b):
        aporb = numpy.dot(a,b)
        escribirMatriz(aporb, "resultado.txt")
    else:
        print "Las matrices no se pueden multiplicar"
except IOError as e:
    print "No existe el archivo '%s'" % e.filename

