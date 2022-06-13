"""REPL cliente de Buddy Simulator
"""
from sys import argv

from tdiagram.REPL import MachineREPL

if __name__ == '__main__':
    if len(argv) != 1:
        print("Uso: python computer_simulator.py")

    repl = MachineREPL()
    repl.cmdloop()