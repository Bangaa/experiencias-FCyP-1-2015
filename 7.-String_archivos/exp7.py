#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Experiencia numero 7 del laboratorio de FCyP.
# Tema: String y archivos


# Funcion que transcribe el menu antiguo al nuevo
# Entrada: el nombre del archivo de entrada y el nombre del archivo de salida
# Salida: Un booleano que indica si se pudo completar la tarea
def transcribeMenu(inputName, outputName):

    # abre ambos archivos es su modo correspondiente
    entrada = open(inputName, "r")
    salida = open(outputName, "w")
    
    plato = entrada.readline().strip()
    precio = entrada.readline().strip()

    while plato != "" and precio != "":
	# escribe en el archivo de salida en el formato pedido
        salida.write("%s: %s\n" % (plato, precio))
        plato = entrada.readline().strip()
        precio = entrada.readline().strip()

    entrada.close()
    salida.close()

    return True

# BLOQUE PRINCIPAL

nombreEntrada = "menu.txt"
nombreSalida = "MenuNuevo.txt"

# EJECUCION

if transcribeMenu(nombreEntrada, nombreSalida) == True:
    print "El menú fue transcrito (Y)"

else:
    print "Hubo un error al ejecutar la transcripcion"

