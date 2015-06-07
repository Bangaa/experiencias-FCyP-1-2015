# Experiencia 8: Listas

## Enunciado

Se tenía un programa que entregaba una lista con los cubos de los números 
naturales entre un número dado y 1 en orden decreciente a partir de un único 
valor n que ingresara un usuario.  El programador que había escrito este 
programa olvidó guardar el programa y perdió todo el código que había escrito, 
sin embargo, en una versión anterior, pensando su solución antes de 
implementarla, había dejado los comentarios de las operaciones que iba a 
realizar. A partir de este código, reconstruye el código que el programador 
perdió, considerando que:

*   Se requiere que se reconstituyan cada una de las funciones de acuerdo a las 
    originales (es decir, cada función debe realizar la tarea asignada y sólo la 
    tarea asignada en los comentarios).
*   Se requiere además la reconstitución del bloque principal del programa.
*   Se debe guardar la estructura del programa que el programador tenía 
    originalmente (es decir, los bloques de entrada, salida y definición de 
    funciones deben estar de acuerdo a los comentarios).

*   El procesamiento que el programa realiza es el siguiente:
    1.  El programa recibe una entrada n y valida que sea un número natural 
        mayor que 0, si no lo es, vuelve a preguntar. Por ejemplo: 5
    2.  Con la entrada validada se crea una lista con los elementos entre 1 y n 
        utilizando una función `crearLista(*)`.  
        Por ejemplo: `[1, 2, 3, 4, 5]`
    3.  Luego la función `elevarAlCubo(*)` recibe el listado para elevar cada 
        uno de los elemento de la lista al cubo.  
        Por ejemplo: `[1, 8, 27, 64, 125]`
    4.  Una última función invierte el orden de los elementos de la lista 
        `invertirLista(*)`.  
        Por ejemplo: `[125, 64, 27, 8, 1]`
    5.  Finalmente se entrega el resultado impreso por pantalla al usuario con 
        `imprimirLista(*)`.  
        Por ejemplo: `125, 64, 27, 8, 1`

*   Se prohíbe usar la función `reverse()` de Python para invertir la lista



## Operaciones sobre listas

### Acceso a los elementos

En alguna clase se explicó, que a los elementos de una lista se les accedía 
mediante un "index", que indicaba la posición del elemento de la lista al cual 
se quería acceder. Esta posicion o index, empieza a contar desde 0, es decir, 
el primer elemento de la lista no está en el lugar 1, sino que en el lugar 0.

```python
lista = [1,2,3,4,5]

i = 0	# primer elemento está en el lugar 0
while i < len(lista):
	print lista[i]
	i += 1			# es lo mismo que: i = i + 1
```

Ejecutando, produce el resultado:

	1
	2
	3
	4
	5

Esto implica que el último elemento está en el lugar `len(lista)-1`, es decir, 
en el lugar 4.

Sin embargo, hay otra forma de acceder al último elemento de la lista; es a 
través de indices negativos, y es así como se ocupa en esta solución. Cuando 
ocupamos indices negativos, se va accediendo desde el último lugar hacia el 
primero. Esto es, en el lugar -1 se encuentra el último elemento, en el lugar 
-2 el penúltimo elemento, y así. Veamos un ejemplo:

```python
lista = [1,2,3,4,5]

i = -1	# el último elemento está en el lugar -1
while i >= -len(lista):
	print lista[i]
	i -= 1			# es lo mismo que: i = i - 1
```

Ejecutando, se muestra lo siguiente:

	5
	4
	3
	2
	1

### Truncar listas

Otra funcionalidad que se usa en la solución, es la facilidad de python para 
cortar listas. Básicamente, uno le entrega dos indices (separados por ':') a la 
lista entre los corchetes, y python devolverá una lista cortada entre esos dos 
indices (el primer indice es incluido solamente):

```python
lista = [1,2,3,4,5]

print lista[1:4]
print lista[1:5]
print lista[1:]
print lista[:4]
```

Imprime:

	  [2,3,4]
	  [2,3,4,5]
	  [2,3,4,5]
	  [1,2,3,4]

Como puede ver, la omision de alguno de los dos indices significa que se 
considerará todo el principio de la lista, o todo el final (dependiendo de cual 
se omita).

Otro ejemplo pero con string (sí, también funciona con strings):

```python
palabra = "Juanito"

print palabra[3:]
```

Imprime:

	nito

Que fácil y bonito.

## Strings/Cadenas con marcas de formato

En varias partes del programa se usa la definición de un string o cadena con 
marcas de formato. Las marcas de formato, son caracteres en la cadena, que son 
reemplazados posteriormente por algún valor en particular, en donde el tipo del 
valor que se reemplaza depende de la marca de formato.

Existen distintas marcas de formato. Algunas son:

 * %d, %i: representa un entero, o número de punto fijo.
 * %f: representa un flotante, o valor decimal
 * %s: representa un string

Un ejemplo:

```python
nombre = "Juanito"

print "a %s no le gustan los %s" % (nombre, "garbanzos")

```

Si se ejecuta el código se obtendrá la siguiente salida:

	a Juanito no le gustan los garbanzos

Como pueden ver, la sintaxis de la cadena con marcas de formato es 
`CADENA_CON_MARCAS % (ARGUMENTOS_A_REEMPLAZAR)`. Los argumentos deben estar en 
el mismo orden que en la cadena, porque así es tal como se van a reemplazar al 
final.  Otro ejemplo:

```python
def funcionInutil(a, b):
	texto = ""

	if a < b:
		texto = "%d es menor que %d" % (a,b)
	
	elif b < a:
		texto = "%d es menor que %d" % (b,a)
	
	else:
		texto = "ambos numeros son iguales"
	
	print texto

funcionInutil(3,4)
funcionInutil(4,4)
funcionInutil(-1,-2)
```

Si se corre el código, se obtendrá lo siguiente:

	3 es menor que 4
	ambos numeros son iguales
	-2 es menor que -1

## Aprender más

Esto y mucho mucho mas, lo puede consultar en el libro [Introducción a la 
programación con python][] (página 67, salida con formato) que está disponible 
en [UsachVirtual][]

[UsachVirtual]: www.usachvirtual.cl/wp/
[Introducción a la programación con python]: http://www.usachvirtual.cl/moodle/mod/resource/view.php?id=273143


