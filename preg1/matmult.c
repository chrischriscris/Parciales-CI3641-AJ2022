/**
 * CI3641 - Lenguajes de Programación I
 * Pregunta 1.b.ii
 * 
 * @author Christopher Gómez (c) 2022
 */
#include <stdio.h>
#include <stdlib.h>

typedef unsigned long int ul;
typedef long int li;

// Separador para imprimir en salida estándar
char *SEP = "========================================\n";

/**
 * create_mat - Asigna memoria para matriz vacía, no inicializada de long int.
 * 
 * @param n Filas de la matriz.
 * @param m Columnas de la matriz.
 * @return Apuntador a la matriz creada.
 */
li **create_mat(ul n, ul m) {
    li **mat = malloc(n * sizeof(li *));
    for (ul i = 0; i < n; i++)
        mat[i] = (li *) malloc(m * sizeof(li));

    return mat;
}

/**
 * read_mat - Lee una matriz de long int de tamaño nxm de la entrada estándar.
 * 
 * @param n: Número de filas de la matriz.
 * @param m: Número de columnas de la matriz.
 * @return Apuntador a la matriz leída.
 */
li **read_mat(ul n, ul m) {
    // Asigna memoria para una matriz de n filas y m columnas
    li **mat = create_mat(n, m);

    for (ul i = 0; i < n; i++)
        for (ul j = 0; j < m; j++)
            scanf("%ld", &mat[i][j]);

    return mat;
}

/**
 * mult_mat - Multiplica dos matrices de long int de tamaño nxm y mxp,
 * respectivamente.
 * 
 * @param A: Primera matriz a multiplicar.
 * @param B: Segunda matriz a multiplicar.
 * @param n: Número de filas de A.
 * @param m: Número de columnas de A y filas de B.
 * @param p: Número de columas de B.
 * @return: Apuntador a la matriz resultado de la multiplicación.
 */
li **mult_mat(li **A, li **B, ul n, ul m, ul p) {
    // Asigna memoria para la matriz resultante
    li **C = create_mat(n, p);

    for (ul i = 0; i < n; i++)
        for (ul j = 0; j < p; j++) {
            C[i][j] = 0;
            for (ul k = 0; k < m; k++)
                C[i][j] += A[i][k] * B[k][j];
        }

    return C;
}

/**
 * Imprime una matriz de enteros de tamaño nxm.
 * 
 * @param A: Matriz a imprimir.
 * @param n: Número de filas de la matriz.
 * @param m: Número de columnas de la matriz.
 */
void print_mat(li **A, ul n, ul m) {
    for (ul i = 0; i < n; i++) {
        for (ul j = 0; j < m; j++)
            printf("%ld\t", A[i][j]);
        printf("\n");
    }
}

/**
 * main - Programa principal.
 *
 * Multiplica dos matrices de tamaño n x m y m x p,
 * mostrando las matrices a multiplicar y la resultante,
 * de dimensión n x p, por salida estándar.
 * 
 * Las matrices se proveen por entrada estándar con el
 * siquiente formato:
 * 
 * <n> <m> <p>
 * <a11> <a12> ... <a1m>
 * <a21> <a22> ... <a2m>
 * ...
 * <an1> <an2> ... <anm>
 * <b11> <b12> ... <b1p>
 * <b21> <b22> ... <b2p>
 * ...
 * <bm1> <bm2> ... <bmp>
 */
int main(int argc, char *argv[]) {
    // Obtiene los tamaños de N, M y P
    ul n, m, p;
    scanf("%lu %lu %lu", &n, &m, &p);

    printf("La dimensión de A es: %lux%lu\n", n, m);
    printf("La dimensión de B es: %lux%lu\n", m, p);
    printf(SEP);

    // Obtiene las matrices de entrada A y B
    li **A = read_mat(n, m);
    li **B = read_mat(m, p);

    // Imprime A y B
    printf("A =\n");
    print_mat(A, n, m);
    printf(SEP);

    printf("B =\n");
    print_mat(B, m, p);
    printf(SEP);

    // Calcula e impime la matriz resultante
    li **C = mult_mat(A, B, n, m, p);
    printf("C = AxB =\n");
    print_mat(C, n, p);

    return 0;
}