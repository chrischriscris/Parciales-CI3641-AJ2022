/**
 * Autor: Christopher Gómez
 * Fecha: 01/Nov/2021
 */

package grafo

import secuencia.*
import kotlin.Double.Companion.POSITIVE_INFINITY

/** 
 * Implementación de búsqueda sobre dígrafos.
 * 
 * @param [g]: grafo sobre el que se ejecuta el algoritmo.
 * @param [s]: Entero no negativo que represente el vértice fuente.
 */
public abstract class Busqueda(val g: Grafo) {
    private var visited = mutableSetOf<Int>()
    abstract val seq: Secuencia<Int>

    /**
     * Realiza un algoritmo
     */
    fun buscar(D: Int, H: Int): Int {
        visited = mutableSetOf<Int>()
        var n = 0
        
        /* 
        if (!g.contains(D))
            throw RuntimeException("El vértice $D no pertenece al grafo.")
        else if (!g.contains(H))
            throw RuntimeException("El vértice $H no pertenece al grafo.")
        */

        // Algoritmo de búsqueda

        // Se añade el primer vértice
        seq.agregar(D)
        while (!seq.vacio()) {
            n++
            
            // El orden lo definirá la implementación de secuencia
            val u = seq.remover()
            if (u == H) {
                while (!seq.vacio()) seq.remover()
                return n
            }

            g.adyacentes(u).forEach { if (visited.add(it)) seq.agregar(it) }
        }
        
        /* H no es alcanzable desde D */
        return -1
    }
}

class BFS(g: Grafo) : Busqueda(g) {
    override val seq = Cola<Int>()
}

class DFS(g: Grafo) : Busqueda(g) {
    override val seq = Pila<Int>()
}