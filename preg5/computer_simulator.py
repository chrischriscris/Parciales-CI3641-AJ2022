"""REPL cliente de Machine Simulator
CI3641 - Lenguajes de Programación I
Pregunta 5

Christopher Gómez (c) 2022
"""
from sys import argv

from tdiagram.REPL import MachineREPL

if __name__ == '__main__':
    if len(argv) != 1:
        print("Uso: python computer_simulator.py")

    repl = MachineREPL()
    repl.cmdloop()