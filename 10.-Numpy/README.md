# Ejemplo Numpy


## Enunciado

Genere un programa en Python que lea dos matrices de dos archivos de texto 
(matrizA.txt y matrizB.txt) y con ellas:

 - Verifique que tienen dimensiones válidas para ser multiplicadas
 - Realice el cálculo de la multiplicación
 - Escriba el cálculo de la multiplicación en un archivo de texto
   “resultado.txt”

En caso de que las dimensiones no sean válidas el archivo "resultado.txt" no 
debe crearse

## Diagrama de procesos

Los procesos que pasaron por mi mente al leer el enunciado se muestran en el 
diagrama a continuación. No es absolutamente necesario escribir el diagrama en 
papel, pero es algo que **TIENEN** que hacer aunque sea en sus mentes antes de 
empezar a escribir siquiera una línea de código.

![Diagrama procesos](https://github.com/Bangaa/experiencias-FCyP-1-2015/raw/numpy/10.-Numpy/diagram.png)

## Tutorial rápido

### Crear un array

Existen varias formas de crear una matriz/array en _Numpy_, que dependen de qué 
es lo que se quiere hacer. Algunas funciones para lograr esto son:

 * __array__ : Es la forma más básica de crear una matriz/array. Se le pasa 
   cualquier objeto que tenga la forma de un array. Recibe además argumentos 
   opcionales que pueden definir la forma que tendrá la matriz. Ejm:

```python console
>>> import numpy
>>> a = numpy.array(["1","2","3","4"], dtype='int') # se especifica que los elementos son de tipo entero
>>> a
array([1, 2, 3, 4])
```

Fíjese que el array `a` tiene todos los elementos de tipo `int` (números 
enteros). Sin el argumento `dtype` los elementos del array serían todos de tipo 
`str` (palabras, cadenas, strings, etc) lo que sería intrabajable en el 
problema.

 * __zeros, ones__: Crea un array con 'ceros 'y 'unos' respectivamente. Se debe 
   especificar la 'forma' (dimensiones) del array en forma de tupla.

```python console
>>> ceros = numpy.zeros( (3,3) )
>>> ceros
array([[ 0.,  0.,  0.],
       [ 0.,  0.,  0.],
       [ 0.,  0.,  0.]])
>>> unos = numpy.ones( (2,3) , dtype='int') # se especifica el tipo
>>> unos
array([[1, 1, 1],
       [1, 1, 1]])
```

 * __arange__ : Es el equivalente a la función `range` de Python.

```python console
>>> rango = numpy.arange(0,10,2)
>>> rango
array([0, 2, 4, 6, 8])
```

 * __linspace__ : Cuando la función `arange` es usada, no se puede predecir el 
   número de elementos que tendrá el array una vez creado, debido a la 
   precisión de los números flotantes. Para solucionar este problema se ocupa 
   la función `linspace`, que especifica la cantidad de elementos que tendrá el 
   array.

```python console
>>> from numpy import pi
>>> numpy.linspace( 0, 2, 9 )		# 9 números desde el 0 hasta el 2
array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ,  1.25,  1.5 ,  1.75,  2.  ])
>>> x = numpy.linspace( 0, 2*pi, 100 )	# útil para evaluar o graficar una función en muchos puntos
>>> f = numpy.sin(x)			# array con el resultado de la evaluación de 'x' en sin()
```

