/**
 * Autor: Christopher Gòmez
 * Fecha: 31/Jul/2022
 */

package secuencia

/**
 * Interfaz para la implementación de la estructura de datos
 * Secuencia, que representa una colección de elementos con orden.
 */ 
public abstract class Secuencia<T> {
    val elems = mutableListOf<T>()

    /** Agrega [el] a la secuencia. */
    fun agregar(el: T) {
        elems.add(el)
    }

    /** Elimina un elemento de la secuencia y lo retorna. */
    abstract fun remover(): T

    /** Retorna un booleano indicando si la secuencia está vacía. */
    fun vacio() = elems.isEmpty()
}