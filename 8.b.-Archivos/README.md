# Experiencia 8 (versión 2015): Archivos
---

## Enunciado

Se desea crear un programa que genere una matriz de n filas y m columnas de 
números aleatorios. Estos números deben ser del conjunto de los naturales y 
además, se requiere como restricción que los números de una misma fila sean 
distintos entre sí.  Una vez generada la matriz, se desea escribir un archivo 
"matriz.txt" con la matriz resultante.  

## Funciones del modulo random

La documentacion se saca de la [pagina oficial de python][doc] y se traduce al 
español.

[doc]: https://docs.python.org/2/library/random.html#random.randrange (documentacion de funciones de random)

* `random()`:  
  Devuelve el siguiente numero flotante aleatorio en el rango [0.0, 1.0[

* `randint(a,b)`:  
  Devuelve un entero aleatorio N tal que `a <= N <= b`.

* `uniform(a,b)`:  
  Devuelve un numero flotante aleatorio N tal que `a <= N <= b` si `a <= b`, y 
  `b <= N <= a` si `b < a`.

* `ranrange(stop)`  
  `randrange(start,stop[,step])`  
  Devuelve un elemento aleatorio seleccionado desde `range(start, stop, step)`. 
  Esta función es equivalente a usar `choice(range(start, stop, step))`

