/**
 * CI3825 - Lenguajes de Programación I
 * Pregunta 1.b.ii
 * 
 * @author Christopher Gómez (c) 2022
 */
#include <stdio.h>
#include <stdlib.h>

/**
 * main - Programa principal.
 *
 * Multiplica dos matrices de tamaño n x m y m x p,
 * imprimendo la matriz resultante de dimensión n x p
 * por salida estándar.
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
 * 
 * La salida tiene el siguiente formato:
 * <c11> <c12> ... <c1p>
 * <c21> <c22> ... <c2p>
 * ...
 * <cn1> <cn2> ... <cnp>
 */
int main(int argc, char *argv[]) {
    // Obtiene los tamaños de N, M y P
    int n = 0, m = 0, p = 0;
    scanf("%d %d %d", &n, &m, &p);

    int a[n][m], b[m][p], c[n][p];

    // Obtiene las matrices de entrada A y B
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) 
            scanf("%d", &a[i][j]);

    for (int i = 0; i < m; i++)
        for (int j = 0; j < p; j++)
            scanf("%d", &b[i][j]);

    // Efectúa la multiplicación
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < p; j++) {
            c[i][j] = 0;
            for (int k=0; k<m; k++) {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }

    // Imprime la matriz resultante
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            printf("%d ", c[i][j]);
        }
        printf("\n");
    }

    return 0;
}