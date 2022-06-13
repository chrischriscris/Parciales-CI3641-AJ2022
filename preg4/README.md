# Pregunta 4)

Se desea que modele e implemente, en el lenguaje de su elección, un módulo que defina el tipo de los cuaterniones y operadores aritméticas sobre estos.
## Cómo usar

Para usar el módulo, incluya en el directorio de su proyecto los archivos `Cuaternion.cpp` y `Cuaternion.hpp`. Podrá usar la clase Cuaternion con todas sus implementaciones incluyendo el header con la directiva de preprocesador

```cpp
#include "Cuaternion.hpp"
```

El módulo implementa la clase Cuaternion, una instancia de esta clase se crea mediante el constructor, que puede recibir cuatro, tres, dos, uno o ningún argumento.

Las instancias de la clase se valen de los operadores sobrecargados `+`, `*`, `~` y `&`, para implementar las operaciones de suma, multiplicación, conjugada y norma de cuaterniones. 

Es válida la suma y multiplicación entre dos cuaterniones y entre un cuaternión y un entero o flotante a la derecha.

En tanto, los operadores de conjugada y norma son unarios, y obtienen respectivamente la conjugada y la norma del cuaternión.

Para correr la suite de tests del programa clone la estructura de archivos, sitúese en la raíz y escriba:

```shell
> make
> runtests
```


```shell
> coverage run tests.py
> coverage report -m
```
