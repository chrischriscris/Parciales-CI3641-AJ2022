# Pregunta 1b)

Implemente los siguientes programas en el lenguaje escogido:

i. Potenciación modulada.

ii. Multiplicación modular.

## Cómo usar

Para construir los programas en sistemas operativos basados en Unix, abra la terminal en el directorio donde está el código fuente y escriba:

```
> make
```

Se generarán dos ejecutables con los nombres `powermod` y `matmuñt`.

### `powermod`

Es una herramienta simple de línea de comandos que permite calcula la potencia modulada (a^b) mod c, donde a y b son enteros no negativos y c > 2, un ejemplo de su uso es el siguiente:


```
> powermod 2 8 250
(2^8) mod 250 = 6
```

El comportamiente de la herramienta es indeterminado de recibir números fuera del rango especificado o parámetros que no sean enteros.

### `matmult`

El programa recibe por entrada estándar información de dos matrices de números enteros a multiplicar, de tamaño m x n y n x p em un formato específico e imprime por salida estándar el resultado de la multiplicación entre ambas. El formato es el siguiente (también disponible en la documentación en el código fuente):

n m p
a11 a12 ... a1m
a21 a22 ... a2m
...
an1 an2 ... anm
b11 b12 ... b1p
b21 b22 ... b2p
...
bm1 bm2 ... bmp

Puede usar de ejemplo `in_matmult1` y  `in_matmult2`, de la siguiente forma:
```
> matmult < in_matmult2
La dimensión de A es: 2x3
La dimensión de B es: 3x2
========================================
A =
1	5	4	
2	1	3	
========================================
B =
0	1	
8	0	
4	2	
========================================
C = AxB =
56	9	
20	8	
```
