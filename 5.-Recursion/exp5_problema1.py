#!/usr/bin/python
# -*- coding: utf-8 -*-


def cuantosCigarros(n):
    sobran = n % 5
    cuantos = n/5

    if cuantos > 0:
        cuantos = cuantos + cuantosCigarros(cuantos + sobran)

    return cuantos

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

