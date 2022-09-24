# 2021 S2 Laboratorio 3

## Instrucciones Generales
- El archivo **debe** llamarse **Laboratorio3.py**
- Debe realizar la siguiente función con iteraciones
- Recordar el uso de los comentarios
- Hora de entrega **10pm del 16 de Setiembre**


## sumarPorIndices(listaNumeros, listaIndices) Valor 5 puntos
- Escibir una función llamada **sumarPorIndices** que recibe los parámetros **listaNumeros** y **listaIndices** 
- Debe validarse que la primera lista debe tener solo valores numéricos, es decir enteros y flotantes, además la segunda lista debe tener solo valores enteros.
- La lista de números y operadores deben de ser del mismo tamaño
- Hacer uso de los **Try y Except**, en el caso de que encuentre un error con los indices **NO** detener la ejecución de las operaciones

```python

>>> sumarPorIndices([12,53.2, -8], [2, 2, 0])
-4
>>> sumarPorIndices([12,53.2, -8], [2, 2, 8])
-16
>>> sumarPorIndices([12,"53.2", -8], [2, 2, 8])
"Error: No se puede sumar valores tipo String"
>>> sumarPorIndices([5], 0)
"Error: Error: El parámetro listaNumeros debe ser tipo Lista"
>>> sumarPorIndices(5, [0])
"Error: Error: El parámetro listaIndices debe ser tipo Lista"
```

## operacionesPorIndices(listaNumeros, listaIndices, listaOperadores) Valor 5 puntos
- Escibir una función llamada **operacionesPorIndices** que recibe los parámetros **listaNumeros** , **listaIndices** y **listaOperadores** 
- Debe validarse que la primera lista debe tener solo valores numéricos, es decir enteros y flotantes, además la segunda lista debe tener solo valores enteros
- La tercera lista debe tener la lista de operadores  a realizar, esto debe apicarse en orden según el índice de lectura.
- Las operaciones permitidas son, +, -, /, *, //, **, %(módulo)
- La lista de números, operadores y la lista de índices deben de ser del mismo tamaño
- Hacer uso de los **Try y Except**, en el caso de que encuentre un error con los indices **NO** detener la ejecución de las operaciones

```python
>>> operacionesPorIndices([12,53.2, -8], [2, 2, 0], ["+", "+", "*"])
192
>>> operacionesPorIndices([12,53.2, -8], [2, 2, 8], ["+", "+", "+"])
-16
>>> operacionesPorIndices([12,"53.2", -8], [2, 2, 8], ["-", "/", "*"])
"Error: No se puede sumar valores tipo String"
>>> operacionesPorIndices([5], 0, ["//"])
"Error: Error: El parámetro listaNumeros debe ser tipo Lista"
>>> operacionesPorIndices(5, [0], ["-"])
"Error: Error: El parámetro listaIndices debe ser tipo Lista"
>>> operacionesPorIndices([5], [0], ["$"])
"Error: Error: Operador no identificado"
```

## convertirBase( lista, baseOrigen, baseDestino). Valor 10 puntos.
- Escriba una función llamada **convertirBase** que reciba como parámetro de entrada una **lista** con diferentes elementos y otros 2 parámetros que son la **base de origen** y la **base de destino** que dicta a hacia donde hacer la conversión. Evitar funciones built-in.
- Debe validarse que el contendido de la lista debe ser entero de un solo dígito o string válidos en el caso de que la base origen sea hexadecimal

```python
>>> convertirBase( [0,0,1,0] , 2, 10)
2
>>> convertirBase( [2] , 10, 2)
10
>>> convertirBase( ["F","F","F"] , 16, 10)
4095
>>> convertirBase( [4,0,9,5] , 10, 16)
"FFF"
>>> convertirBase( [7] , 10, 4)
13
>>> convertirBase( [1,3] , 4, 10) 
7
>>> convertirBase( [2,5,3] , 10, 7)
511
>>> convertirBase( [5,1,1] , 7, 10)
253
```
