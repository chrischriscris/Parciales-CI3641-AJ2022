KC = kotlinc
KFLAGS = -cp

all: Pila.class Cola.class

Pila.class: Secuencia.class Pila.kt
	$(KC) $(KFLAGS) . Pila.kt

Cola.class: Secuencia.class Cola.kt
	$(KC) $(KFLAGS) . Cola.kt

Secuencia.class: Secuencia.kt
	$(KC) Secuencia.kt

Grafo.class: Grafo.kt
	$(KC) Grafo.kt

clean:
	rm -rf *.class META-INF
