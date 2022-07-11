"""REPL cliente de Buddy Simulator
CI3641 - Lenguajes de Programación I
Pregunta 3

Christopher Gómez (c) 2022
"""

from sys import argv
from boolev.REPL import BooleanEvaluatorREPL

if __name__ == '__main__':
    if len(argv) != 1:
        print(f"Uso: python {argv[0]}")

    repl = BooleanEvaluatorREPL(n)
    repl.cmdloop()