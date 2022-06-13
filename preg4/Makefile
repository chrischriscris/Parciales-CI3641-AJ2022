CC = g++
CFLAGS = -Wall

all: src/Cuaternion.o runtests

runtests: tests/tests.cpp src/Cuaternion.o
	$(CC) $(CFLAGS) -o runtests tests/tests.cpp src/Cuaternion.o

src/Cuaternion.o: src/Cuaternion.cpp
	$(CC) $(CFLAGS) -c src/Cuaternion.cpp -o src/Cuaternion.o

clean:
	rm src/*.o runtests