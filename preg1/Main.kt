import secuencia.*
import grafo.*

fun main() {
    println("Prueba de la clase Grafo")
    val g = Grafo()
    g.agregarVertice(0)
    g.agregarVertice(13)
    g.agregarVertice(14)
    g.agregarLado(1, 2)
    g.agregarLado(1, 7)
    g.agregarLado(1, 8)
    g.agregarLado(2, 3)
    g.agregarLado(2, 6)
    g.agregarLado(3, 4)
    g.agregarLado(3, 5)
    g.agregarLado(8, 9)
    g.agregarLado(12, 8)
    g.agregarLado(9, 10)
    g.agregarLado(11, 9)

    println("DFS:")
    var dfs = DFS(g)
    println("Total de nodos: ${dfs.buscar(1, 2)}")
    println("Total de nodos: ${dfs.buscar(1, 10)}")
    println("Total de nodos: ${dfs.buscar(1, 14)}")


    println("BFS:")
    var bfs = BFS(g)
    println("Total de nodos: ${dfs.buscar(1, 2)}")
    println("Total de nodos: ${bfs.buscar(1, 10)}")
    println("Total de nodos: ${bfs.buscar(1, 14)}")
}