# 2021 S2 Laboratorio 5

## Instrucciones Generales
- El archivo **debe** llamarse **Laboratorio5.py**
- Debe realizar la siguiente función con recursión de cola

## Ejercicio 1. Valor 20 puntos.
Escriba una función llamada eliminarRepetidos que reciba como parámetro de entrada una lista con diferentes elementos es decir enteros, flotantes y cadenas de texto, y eliminar si un elemento de esta lista aparece más de una vez. Hacer uso de la recursión y evitar funciones built-in.

```python
>>> eliminarRepetidos( [12, 78, 12, 0, 5.2, "abc", 0, 12, 5.2, 12] )
[78, "abc"]
>>> eliminarRepetidos( [12, 5.2, 12] )
[ 5.2]
```

## Ejercicio 2. Valor 20 puntos.
Escriba una función sumaImparesPares (lista1 , lista2) que reciba dos lista de números, y retorne una lista que contenga la suma de las posiciones pares de las dos listas de la misma manera con las posiciones impares. No puede usar len (), solo puede recorrer la lista una vez. La función debe comportarse de la siguiente manera:

```python
>>> sumaImparesPares([0,2,3,4], [4, 8, 6, 0])
[13, 14]
>>> suma([10, 0], [100, 2])
[110, 2]
 >>> suma([1,2], "dos")
 "Error: segundo argumento debe ser entero"
 ```

## Ejercicio 3. Valor 20 puntos.
Escriba una función llamada convertirBase que reciba como parámetro de entrada una lista con diferentes elementos y otros 2 parámetros que son la base de origen y de destino que dicta a hacia donde hacer la conversión. Hacer uso de la recursión y evitar funciones built-in.

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
