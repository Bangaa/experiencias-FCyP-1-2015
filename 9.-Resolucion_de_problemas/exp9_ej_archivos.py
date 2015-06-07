#!/usr/bin/python
# -*- coding: utf-8 -*-

    # FUNCIONES

# Indica cuantas veces aparece la palabra 'pal' en el archivo con el nombre 
# 'filename'
#
# @param pal        Palabra que se cuenta en el archivo
# @param filename   Nombre del archivo en el que se busca la palabra
#
# @return Cuantas veces aparece la palabra 'pal' en el archivo 'filename'
def contarPalabras(pal, filename):
    matriz = archivoAMatrix(filename)

    cont = 0

    for fila in matriz:

        if palabra in fila:
            cont += 1 

    return cont

# Le quita los elementos vacios a una lista de strings
#
# @param lista  Lista a la que se le quitan los elementos vacios
#
# @return Una copia de la lista sin los elementos vacios ('')
def listaSinVacios(lista):
    sinvacios = []

    for elem in lista:
        if elem != "":
            sinvacios.append(elem)

    return sinvacios

# Imprime una lista de listas en forma de matriz
#
# @param matrix Es la matriz que se quiere imprimir
# @return Nada
def imprimirMatrix(matrix):
    for fila in matrix:
        print fila

# Función que imprime los elementos de una lista en una sola línea
# Entrada: Lista de numeros
# Salida: Nada. Imprime la lista de numeros separados por coma
def imprimirLista(lista):
    text = "%d" % lista[0]

    for elem in lista[1:]:
        text += ", %d" % elem

    print text

# Convierte un archivo a una matriz, donde cada fila de la matriz es una lista 
# con cada palabra de la linea correspondiente. Se asume como separador de 
# palabras a los puntos, espacios y saltos de linea.
#
# @param filename   Es el nombre del archivo que se convierte a matriz
#
# @return Una matriz de strings
def archivoAMatrix(filename):
    separadores = " .\n"
    matrix = []

    archivo = open(filename, "r")

    for linea in archivo:
        lista = []
        palabra = ""

        for letra in linea:
            if letra not in separadores:
                palabra += letra

            else:
                lista.append(palabra)
                palabra = ""
        
        lista = listaSinVacios(lista) 
        matrix.append(lista) 

    archivo.close()
    return matrix

# Obtiene en que lineas aparece la palabra 'palabra' en el archivo 'filename'.  
# Esta informacion se devuelve en forma de lista.
#
# @param palabra    Es la palabra que se busca en el archivo
# @param filename   Es el nombre del archivo
#
# @return Una lista con los numeros de linea en donde aparece la palabra
def obtenerNumLineas(palabra, filename):
    lineas = []

    matriz = archivoAMatrix(filename)
    i = 0

    while i < len(matriz):
        if palabra in matriz[i]:
            lineas.append(i+1)  # i+1 ya que los archivos no tienen linea 0
        i += 1

    return lineas




    # ENTRADA
# Se pide una palabra al usuario para ser buscada en el archivo 'lectura.txt'

palabra = raw_input("Ingrese una palabra: ")

    # PROCESAMIENTO
# Se cuenta cuantas veces aparece la palabra en el archivo 'lectura.txt' y se 
# busca en que lineas se encuentra la palabra

cuantas = contarPalabras(palabra, "lectura.txt") 
lineas  = obtenerNumLineas(palabra, "lectura.txt")

    # SALIDA
# Se escribe en el archivo de salida 'reporte.txt' cuantas veces aparece la 
# palabra en el archivo y en que lineas aparece la palabra

salida = """La palabra: %s
Aparece en el texto %d veces
En las lineas
""" % (palabra, cuantas)

for num in lineas:
    salida += "%d, " % (num)
salida += "\n"

output = open("reporte.txt", "w")

output.write(salida)

output.close()
