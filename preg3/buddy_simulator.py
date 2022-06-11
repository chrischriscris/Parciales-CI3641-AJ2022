"""REPL cliete de Buddy Simulator
"""

from sys import argv, exit
from balloc.REPL import BuddySystemREPL

if __name__ == '__main__':
    if len(argv) != 2:
        print("Uso: python buddy_simulator.py <# de bloques>")
    else:
        try:
            n = int(argv[1])
            if n < 0:
                print("El número de bloques deber ser positivo")
                exit(1)
            elif n & (n-1) or not n:
                print("El número de bloques deber ser una potencia de base 2 positiva")
                exit(1)

            repl = BuddySystemREPL(n)
            repl.cmdloop()
        except ValueError:
            print("El número de bloques debe ser un número entero")