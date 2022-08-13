CC = gcc
CFLAGS = -std=c99 -Wall

all: powermod matmult

matmult: matmult.c
	$(CC) $(CFLAGS) -o matmult matmult.c

powermod: powermod.c
	$(CC) $(CFLAGS) -o powermod powermod.c

clean:
	rm powermod matmult