"""REPL cliente de Buddy Simulator
CI3641 - Lenguajes de Programación I
Pregunta 3

Christopher Gómez (c) 2022
"""

from sys import argv
from balloc.REPL import BuddySystemREPL

if __name__ == '__main__':
    if len(argv) != 2:
        print("Uso: python buddy_simulator.py <# de bloques>")
    else:
        try:
            n = int(argv[1])
            repl = BuddySystemREPL(n)
            repl.cmdloop()
        except ValueError as e:
            print("El número de bloques deber ser una potencia de "
                "base 2 positiva")