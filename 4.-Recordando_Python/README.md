# Experiencia 4: Recordando Python

## Enunciado

Un colegio de Estación Central está enseñando a los niños de quinto básico el 
cálculo de área  y  perímetro  de  diferentes figuras  geométricas,  y 
requiere  de  un  programa  escrito  en Python para que sus alumnos puedan 
verificar  los resultados que obtienen. En  particular, están  solicitando que 
el  programa  maneje  círculos,  triángulos rectángulos ,  rectángulos  y 
cuadrados. La siguiente tabla resume la materia vista por los alumnos:

| Figura | Fórmula | Requiere conocer: |
| ----- | ----- | ----- |
| Círculo | A = pi * r^2; P = 2 * pi * r | **r**: radio (cm) |
| Triángulo rectángulo | A = b * h/2; P = b + h + sqrt(b^2 + h^2) | **b**: base (cm); **h**: altura (cm) |
| Rectángulo | A = b * h; P = 2 * (b + h) | **b**: base (cm); **h**: altura (cm) |
| Cuadrado | A = a^2; P = 4 * a | **a**: longitud del lado (cm) |


## Análisis

Claramente  podemos  crear  cuatro funciones  que  calculen  el  área  y cuatro 
funciones  que calculen el perímetro de las figuras geométricas. Como estas 
funciones serían más útiles si puede n ser  usadas en  alguna  expresión 
aritmética , sería incorrecto agregar  entrada  de datos o salida de datos en 
ellas .  Así, procuraremos que la única comunicación con estas funciones sea a 
través de los parámetros y el valor que devuelven.

¿Pero cómo hacemos para saber qué figura geométrica se quiere trabajar?

Esto  necesita  de una instrucción por  parte del  usuario.  Crearemos  una 
función  que despliegue  en  pantalla  un menú ,  le  pida  al  usuario  que 
indique  qué  figura  geométrica quiere  trabajar  y  que  devuelva  la  opción 
seleccionada .  En  este  caso  el objetivo de  la función es interactuar con 
el usuario , por lo que no es incorrecto que realice entrada y salida de datos. 
El menú sería algo como:


    MENU
    =======

    Opción 1: Área y perímetro de un círculo
    Opción 2: Área y perímetro de un triángulo rectángulo
    Opción 3: Área y perímetro de un rectángulo
    Opción 4: Área y perímetro de un cuadrado

    Elija una opción:
