/**
 * CI3641 - Lenguajes de Programación I
 * Pregunta 2.b.i
 * 
 * @author Christopher Gómez (c) 2022
 */
#import <Foundation/Foundation.h>
#import <omp.h>
#import <stdio.h>

typedef unsigned long int ul;

/**
 * vec_dot_product - Calcula el producto punto entre dos vectores.
 * 
 * Aprovecha mecanismos de concurrencia y paraleliza los cálculos.
 *
 * Óptimo cuando los vectores tienen millones de componentes.
 * 
 * @param u: Primer vector.
 * @param v: Segundo vector.
 * @return: Resultado del producto punto.
 */
double vec_dot_product(NSMutableArray *u, NSMutableArray *v, ul n) {
    ul i;
    double res = 0;

    #pragma omp parallel \
        shared( n, u, v ) \
        private( i )
    #pragma omp for reduction( + : res )
    for (i = 0; i < n; i++)
        res += [[u objectAtIndex:i] doubleValue] * [[v objectAtIndex:i] doubleValue];

    return res;
}

/**
 * main - Programa principal.
 *
 * Calcula el producto punto de dos vectores de tamaño
 * n aprovechando mecanismos de concurrenncia. Muestra
 * el resultado por salida estándar.
 *
 * Los vectores se proveen por entrada estándar con el
 * siquiente formato:
 * 
 * <n> 
 * <u1> <u2> ... <un>
 * <v1> <v2> ... <vn>
 */
int main(int argc, char *argv[]) {
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];

    // Obtiene el tamaño de u y v.
    ul n, i;
    scanf("%lu", &n);

    // Obtiene los vectores de entrada u y v en arreglos mutables
    NSMutableArray *u = [NSMutableArray array];
    for (i = 0; i < n; i++) {
        double el;
        scanf("%lf", &el);
        [u addObject:[NSNumber numberWithDouble: el]];
    }

    NSMutableArray *v = [NSMutableArray array];
    for (i = 0; i < n; i++) {
        double el;
        scanf("%lf", &el);
        [v addObject:[NSNumber numberWithDouble: el]];
    }

    // Calcula e imprime el producto punto resultante
    printf("<u, v> = %lf\n", vec_dot_product(u, v, n));

    [pool release];
    return 0;
}