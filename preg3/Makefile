CC = g++
CFLAGS = -Wall

all: cuaternion

cuaternion: cuaternion.o
	$(CC) $(CFLAGS) -o cuaternion Cuaternion.o

cuaternion.o: src/Cuaternion.hpp
	$(CC) $(CFLAGS) -c src/Cuaternion.cpp

clean:
	rm *.o cuaternion