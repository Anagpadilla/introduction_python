# -*- coding: utf-8 -*-
"""Bucles.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xzg34xMAOVizBJtZLsdyBBwXKaRFt24i

# Bucles

![fair.png](data:image/png;base64,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)

Cuando queremos hacer algo más de una vez (*iterar*) necesitamos un **bucle** y Python nos ofrece dos opciones para ello: `while` y `for`.

## Repetir con `while`

El mecanismo más sencillo en Python para repetir instrucciones es mediante la sentencia `while`. Veamos un sencillo bucle que muestra los números del 1 al 5:
"""

contador = 0
while contador <= 5:
    print(contador)
    contador = contador + 1

"""La *condición* del bucle se comprueba en cada nueva repetición. En este caso chequeamos que la variable `contador` sea menor o igual que 5. Dentro del *cuerpo* del bucle estamos incrementando esa variable en 1 unidad.

### Bucle Infinito

Si queremos repetir hasta que algo suceda, pero no estamos seguros cuándo podría ocurrir, podemos escribir un *bucle infinito* con una sentencia `break`.

Veamos un ejemplo leyendo una entrada desde teclado con la función `input()` hasta que se pulse la letra "q":
"""

while True:
    texto = input('Introduce aquí texto [type q to quit]: ')
    if texto == 'q':
        break
    print( texto )

"""> Suele ser común, especialmente en principiantes, equivocarnos en la definición de la condición y obtener bucles infinitos. La revisión del código nos permitirá descubrir qué está ocurriendo.

### Continuar un bucle

Hay veces que no queremos romper un bucle sino simplemente queremos saltar adelante hacia la siguiente repetición. Veamos un ejemplo en el que leemos un entero y mostramos su cuadrado si el número es impar o lo saltamos si es par:
"""

while True:
    valor = input('Introduce un entero [q to quit]: ')
    if valor == 'q':
        break
    numero = int(valor)
    if numero % 2 == 0:
        print( 'Es par, saltamos el bucle' )
        continue
    cuadrado = numero * numero
    print( numero, 'el cuadrado es: ', cuadrado)

"""## Iterar con `for`

Python hace uso frecuentemente de **iteradores**.

Esto hace posible *recorrer* estructuras de datos sin conocer el tamaño que tienen o cómo están implementadas. Incluso es posible iterar sobre datos que se crean sobre la marcha, permitiendo el acceso a flujos de datos (*data streams*) que, de otra manera, no cabrían de una vez en la memoria de la máquina.

Para mostrar una iteración necesitamos algo sobre lo que iterar: **iterables**. Veamos un ejemplo con las cadenas de texto:

Recorrer la cadena de forma "*tradicional*":
"""

palabra = 'abcd'
indice = 0
while indice < len(palabra):
    print(palabra[indice])
    indice = indice + 1

"""Pero hay una manera mejor y más "*pitónica*":"""

for letra in palabra:
    print(letra)

"""### Ejercicio

Dada una cadena de texto, indique el número de vocales que contiene:

#### Ejemplo:

➡️ `holaestoesunapruebaenpython`  
⬅️ 12
"""

# Escriba aquí su solución

def contar_vocales(texto):
	contador = 0
	for letra in texto:
		if letra.lower() in "aeiou":
			contador += 1
	return contador

texto = 'holaestoesunapruebaenpython'
cantidad = contar_vocales(texto)
print('En el texto:', (texto), 'hay:', (cantidad), 'vocales.')

"""## Generar secuencias de números

La función `range()` devuelve un flujo de números en el rango especificado, sin necesidad de crear y almacenar previamente una larga estructura de datos. Esto permite generar rangos enormes sin consumir toda la memoria del sistema.

El uso de `range()` es similar a los *slices*: `range(start, stop, step)`. Podemos omitir `start` y el rango empezaría en 0. El único valor requerido es `stop` y el último valor generado será el justo anterior a este. El valor por defecto de `step` es 1, pero se puede ir "hacia detrás" con -1.

`range()` devuelve un objeto *iterable*, así que necesitamos obtener los valores paso a paso con una sentencia `for ... in` (o convertir el objeto a una secuencia como una lista).

Veamos un ejemplo generando el rango $[0, 1, 2]$
"""

for x in range(0, 3):
    print(x)

list(range(0, 3))

"""### Bucles anidados

Es posible escribir un bucle dentro de otro. Esto se conoce como **bucles anidados**.
"""

for i in range(3):
    for j in range(2):
        print(i, j)
    print('---')

"""<h2 id="quiz">Cuestionario sobre Bucles</h2>

Escribe un bucle <code>for</code> que imprima todos los elementos entre <b>-5</b> y <b>5</b> usando la función de rango.
"""

# Escribe tu código debajo y presiona Shift+Enter para ejecutar
for i in range(-5,5): 
  print(i)

"""Imprime los elementos de la siguiente lista: <code>Genres=\[ 'rock', 'R\&B', 'Soundtrack', 'R\&B', 'soul', 'pop']</code>
Asegúrate de seguir las convenciones de Python.

"""

# Escribe tu código debajo y presiona Shift+Enter para ejecutar
genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']

for x in genres:
  print(x)

"""<hr>

Escribe un blucle for que imprima la siguiente lista: <code>squares=\['red', 'yellow', 'green', 'purple', 'blue']</code>
"""

# Escribe tu código debajo y presiona Shift+Enter para ejecutar

squares=['red', 'yellow', 'green', 'purple', 'blue']

for x in squares:
  print(x)

"""<hr>

Escribe un bucle while para mostrar los valores del Rating de una lista de reproducción de un álbum almacenada en la lista <code>PlayListRatings</code>. Si la puntuación es inferior a 6, sal del bucle. La lista <code>PlayListRatings</code> está dada por: <code>PlayListRatings = \[10, 9.5, 10, 8, 7.5, 5, 10, 10]</code>
"""

# Escribe tu código debajo y presiona Shift+Enter para ejecutar
playListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
indice = 0
while indice < len(playListRatings):
    puntuacion = playListRatings[indice]
    if puntuacion < 6:
        break
    print(puntuacion)
    indice=indice + 1

"""Escribe un bucle while para copiar los string <code>'orange'</code> de la lista <code>squares</code> a la lista <code>new_squares</code>. Para y sal del bucle si el valor de la lista no es <code>'orange'</code>:

"""

# Escribe tu código debajo y presiona Shift+Enter para ejecutar

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
#1.Recorrer con while la lista squares
indice = 0
while squares[indice] == 'orange':
  new_squares.append(squares[indice])
  indice = indice + 1
  continue
print(new_squares)

"""### Ejercicio (Opcional)

Imprima los 100 primeros números de la secuencia de Fibonacci: $0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, \dots$

####  Pista: `_`

Hay situaciones en las que no necesitamos usar la variable que toma valores en el rango, únicamente queremos *repetir una acción un número de veces*.

Para estos casos se suele recomendar usar el **subguión** (*guión bajo*) como nombre de variable, que da a entender que no estamos usando esta variable de forma explícita:
"""

for _ in range(10):
    print('Hello world!')

"""> Simplemente hemos mostrado 10 veces el mensaje `Hello world!` sin necesidad usar un contador."""

# Escriba aquí su solución
# Partiendo del 0 y el 1
a = 0
b = 1
#Bucle: