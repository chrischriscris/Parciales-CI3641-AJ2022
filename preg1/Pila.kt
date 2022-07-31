/**
 * Autor: Christopher Gòmez
 * Fecha: 31/Jul/2022
 */

/**
 * Clase que implementa la interfaz Secuencia como una pila.
 *
 * Soporta las operaciones de inserción, borrado y chequeo de
 * si está vacía.
 */ 
class Pila<T>: Secuencia<T> {
    private val elems = mutableListOf<T>()

    /** Agrega [el] a la secuencia. */
    override fun agregar(el: T) {
        elems.add(el)
    }

    /** Elimina un elemento de la secuencia y lo retorna. */
    override fun remover(): T {
        if (vacio()) throw Exception("La pila está vacía.")
        return elems.removeAt(elems.size - 1)
    }

    /** Retorna un booleano indicando si la secuencia está vacía. */
    override fun vacio() = elems.isEmpty()
}