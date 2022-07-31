/**
 * Autor: Christopher Gòmez
 * Fecha: 31/Jul/2022
 */

/**
 * Interfaz para la implementación de la estructura de datos
 * Secuencia, que representa una colección de elementos con orden.
 */ 
interface Secuencia<T> {
    /** Agrega [el] a la secuencia. */
    fun agregar(el: T)

    /** Elimina un elemento de la secuencia y lo retorna. */
    fun remover(): T

    /** Retorna un booleano indicando si la secuencia está vacía. */
    fun vacio(): Boolean
}