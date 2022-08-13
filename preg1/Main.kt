import secuencia.*
import grafo.*

fun main() {
    println("Test implementaciones de búsqueda:\n")
    val g = Grafo()
    val dfs = DFS(g)
    val bfs = BFS(g)

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

    println("Haciendo DFS:\n")
    println("dfs.buscar(1, 2) = ${dfs.buscar(1, 2)}")
    println("dfs.buscar(1, 10) = ${dfs.buscar(1, 10)}")
    println("dfs.buscar(1, 14) = ${dfs.buscar(1, 14)}")

    println("\nHaciendo BFS:\n")
    println("bfs.buscar(1, 2) = ${bfs.buscar(1, 2)}")
    println("bfs.buscar(1, 10) = ${bfs.buscar(1, 10)}")
    println("bfs.buscar(1, 14) = ${bfs.buscar(1, 14)}")

    println("\nTest de excepciones\n")
    try {
        print("bfs.buscar(1, 100) = ")
        println("${bfs.buscar(1, 100)}")
    }
    catch(e: RuntimeException) {
        println("Excepción atajada: ${e.message}")
    }
    try {
        print("dfs.buscar(-10, 1) = ")
        println("${bfs.buscar(-10, 1)}")
    }
    catch(e: RuntimeException) {
        println("Excepción atajada: ${e.message}")
    }
}