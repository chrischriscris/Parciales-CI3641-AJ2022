KC = kotlinc
KFLAGS = -cp

all: Pila.class Cola.class Grafo.class Busqueda.class MainKt

Pila.class: Secuencia.class Pila.kt
	$(KC) $(KFLAGS) . Pila.kt

Cola.class: Secuencia.class Cola.kt
	$(KC) $(KFLAGS) . Cola.kt

Secuencia.class: Secuencia.kt
	$(KC) Secuencia.kt

Grafo.class: Grafo.kt
	$(KC) Grafo.kt

Busqueda.class: Secuencia.class Pila.class Cola.class Busqueda.kt
	$(KC) $(KFLAGS) . Busqueda.kt

MainKt: Main.kt
	$(KC) $(KFLAGS) . Main.kt

run: MainKt
	kotlin MainKt

clean:
	rm -rf *.class META-INF
