/**
 * Autor: Christopher Gòmez
 * Fecha: 31/Jul/2022
 */

import java.lang.StringBuilder

/** 
 * Clase que implementa la estructura de digrafo como una lista de adyacencia.
 * No permite lados repetidos.
 *
 * Soporta las operaciones de añadir un lado y obtener los adyacentes a un
 * nodo.
 */
class Grafo {
    val nVertices
    get() = ady.size

    private val ady = mutableListOf<MutableList<Int>>()
    val nodeMap = mutableMapOf<Int, Int>()

    /**
     * Agrega un lado de [u] a [v] al dígrafo.
     * 
     * @return True si el lado fue agregado exitosamente.
     *     False si ya existía el lado en el grafo.
     */
    fun agregarLado(u: Int, v: Int): Boolean{
        /* Si no existía, añade el nodo a la lista de adyacencias
        inicializado con una lista vacía */
        val node = nodeMap.getOrPut(u) { 
            ady.add(mutableListOf<Int>())
            nVertices - 1
        }

        // Análogamente
        nodeMap.getOrPut(v) {
            ady.add(mutableListOf<Int>())
            nVertices - 1
        }

        return if (v !in ady[node]) ady[node].add(v) else false
    }

    /**
     * Retorna la lista de adyacencia del vértice [u] como un objeto iterable.
     *
     * @throws [RuntimeException] El vértice [u] no está en el grafo.
     */
    fun adyacentes(u: Int): Iterable<Int> {
        if (!contains(u)) throw RuntimeException("Vertice $u no existe")
        return ady[nodeMap[u]!!]
    }

    /**
     * Retorna un booleano indicando si el grafo contiene el nodo dado.
     */
    fun contains(u: Int) = u in nodeMap

    /** 
     * Retorna la representación en String del dígrafo, como
     * una String de múltiples líneas donde cada línea tiene la forma:
     *
     * Vértice  | --> Lista de lados.
     * 
     * El orden de los vértices en la representación no está garantizado.
     */
    override fun toString(): String {
	    val str = StringBuilder()

        for (u in nodeMap.keys) str.append("%4d | ${adyacentes(u)}\n".format(u))

	    return str.toString()
    }
}