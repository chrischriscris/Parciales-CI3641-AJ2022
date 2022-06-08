/**
 * CI3825 - Lenguajes de Programación I
 * Pregunta 1.b.i
 * 
 * @author Christopher Gómez (c) 2022
 */
#include <stdio.h>
#include <stdlib.h>

typedef unsigned long int ul;

/**
 * powermod - Computa el valor de (a^b) mod c utilizando recursión.
 *
 * @param a: base
 * @param b: exponente
 * @param c: modulo
 * @returns (a^b) mod c
 */
ul powermod(ul a, ul b, ul c) {
    if (b == 0) return 1;
    return ( (a % c) * powermod(a, b - 1, c) ) % c;
}

/**
 * main - Programa principal.
 *
 * Calcular el valor de (a^b) mod c, donde a, b y c se proporcionan
 * al programa como argumentos de la línea de comandos.
 */
int main(int argc, char *argv[]) {
    if (argc != 4) {
        printf("Usage: %s a b c\n", argv[0]);
        return 1;
    }

    // Se obtienen tres argumentos de línea de comandos
    ul a, b, c;
    a = atol(argv[1]);
    b = atol(argv[2]);
    c = atol(argv[3]);

    printf("Calculando powermod(%lu, %lu %lu):", a, b, c);
    ul res = powermod(a, b, c);
    printf("    Resultado:%lu\n", res);

    return 0;
}