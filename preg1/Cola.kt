/**
 * Autor: Christopher Gòmez
 * Fecha: 31/Jul/2022
 */

package secuencia

/**
 * Clase que implementa la clase abstracta Secuencia como una cola.
 * 
 * Soporta las operaciones de inserción, borrado y chequeo de
 * si está vacía.
 */
public class Cola<T>: Secuencia<T>() {
    /** Elimina un elemento de la secuencia y lo retorna. */
    override fun remover(): T {
        if (vacio()) throw Exception("La cola está vacía.")
        return elems.removeAt(0)
    }
}