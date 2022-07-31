/**
 * Autor: Christopher Gòmez
 * Fecha: 31/Jul/2022
 */

/**
 * Clase que implementa la interfaz Secuencia como una cola.
 * 
 * Soporta las operaciones de inserción, borrado y chequeo de
 * si está vacía.
 */
class Cola<T>: Secuencia<T> {
    private val elems = mutableListOf<T>()

    /** Agrega [el] a la secuencia. */
    override fun agregar(el: T) {
        elems.add(el)
    }

    /** Elimina un elemento de la secuencia y lo retorna. */
    override fun remover(): T {
        if (vacio()) throw Exception("La cola está vacía.")
        return elems.removeAt(0)
    }

    /** Retorna un booleano indicando si la secuencia está vacía. */
    override fun vacio() = elems.isEmpty()
}