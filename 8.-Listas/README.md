# Experiencia 8: Listas

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


