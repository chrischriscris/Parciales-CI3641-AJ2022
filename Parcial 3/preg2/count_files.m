/**
 * CI3641 - Lenguajes de Programación I
 * Pregunta 2.b.ii
 * 
 * @author Christopher Gómez (c) 2022
 */

#import <Foundation/Foundation.h>
#import <omp.h>

// Variable global para contar los archivos
int size = 0;

/**
 * count_files - Cuenta los archivos dentro del directorio recursivamente.
 * 
 * Aprovecha mecanismos de concurrencia y crea un hilo por cada subdirectorio.
 * 
 * @param path: path al directorio raíz.
 * @return: 1 si la opreación fue exitosa
 *     0 de otra forma
 */
int count_files(NSString *path) {
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];

    /* Arreglo y de hilos que crea */
    int local_size = 0;

    // Inicializa un NSFileManager
    NSFileManager *fm = [NSFileManager defaultManager];
    NSError *err = [NSError alloc];

    BOOL isDir = NO;
    BOOL exists = [fm fileExistsAtPath:path isDirectory:&isDir];
    if (exists && isDir) {
        // Explora los contenidos del directorio
        NSArray *dirArray = [fm contentsOfDirectoryAtPath:path error:&err];
        NSString *subPath = nil;

        // Para cada archivo en el directorio
        for (NSString *str in dirArray) {
            // Construye el nuevo path
            subPath = [path stringByAppendingPathComponent:str];
            BOOL issubDir = NO;
            [fm fileExistsAtPath:subPath isDirectory:&issubDir];

            // Si es directorio, hace una llamada recursiva en paralelo
            if (issubDir)
                #pragma omp task shared(size)
                { count_files(subPath); }
            else local_size++;
        }
    } else {
        printf("El directorio no existe.\n");
        return 0;
    }

    // Actualiza la variable de forma atómica
    #pragma omp atomic update
    size += local_size;

    // Espera que terminen los subhilos
    #pragma omp taskwait

    [pool drain];

    return 1;
}

/**
 * main - Programa principal.
 *
 * Cuenta los archivos dentro del directorio recursivamente.
 */
int main(int argc, const char *argv[]) {
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];

    if (argc != 2) {
        printf("Uso: %s <rootDirectory>\n", argv[0]);
        return 1;
    }

    NSString *root = [NSString stringWithUTF8String:argv[1]];

    #pragma omp parallel
    #pragma omp single
    if (count_files(root))
        printf("El directorio %s tiene %d archivos\n", argv[1], size);

    [pool drain];
    return 0;
}