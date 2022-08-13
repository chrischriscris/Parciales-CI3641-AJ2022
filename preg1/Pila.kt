/**
 * Autor: Christopher Gòmez
 * Fecha: 31/Jul/2022
 */

package secuencia

 /**
 * Clase que implementa la interfaz Secuencia como una pila.
 *
 * Soporta las operaciones de inserción, borrado y chequeo de
 * si está vacía.
 */ 
public class Pila<T>: Secuencia<T>() {
    /** Elimina un elemento de la secuencia y lo retorna. */
    override fun remover(): T {
        if (vacio()) throw Exception("La pila está vacía.")
        return elems.removeAt(elems.size - 1)
    }
}