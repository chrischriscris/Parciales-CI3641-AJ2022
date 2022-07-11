"""Módulo que implementa un evaluador de expresiones booleanas.
CI3641 - Lenguajes de Programación I
Pregunta 2

Christopher Gómez (c) 2022
"""
from typing import Tuple
import ply.lex as lex
import ply.yacc as yacc

from boolev import grammar, tokenrules

class BooleanEvaluator:
    """Clase que implementa un evaluador de expresiones booleanas prefijas
    y posfijas.

    Atributos:
        lex:
            Instancia de Lexer con el analizador lexicográfico
            generado por ply.
        parser:
            Instancia del Parser con el analizador sintáctico
            generado por ply.
        bin_operators:
            Lista con los operadores binarios del evaluador
        un_operators:
            Lista con los operadores unarios del evaluador
    """
    def __init__(self):
        # No se imprime ningún mensaje que pueda generar ply
        self.lex = lex.lex(module=tokenrules)
        self.parser = yacc.yacc(module=grammar)
        self.bin_operators = ['=>', '&', '|']
        self.un_operators = ['^']

    def parse(self, command: str, prefix: bool) -> Tuple[str, bool]:
        """Llama al parser de BooleanEvaluator.

        Retorna:
            Una tupla (string infija, evaluación) con el resultado del parsing.
        """
        if prefix:
            return self.parser.parse(self.to_posfix(command), lexer=self.lex)
        return self.parser.parse(command, lexer=self.lex)

    def evaluate(self, command: str, posfix: bool = False) -> str:
        """Evalúa la expresión dada.
        
        Retorna:
            Una representación en string del resultado de la evaluación.
        """
        return str(self.parse(command, posfix)[1]).lower()

    def show(self, command: str, posfix: bool = False) -> str:
        """Convierte la expresión a su forma infija.

        Retorna:
            Una representación en string de la expresión introducida en el
            comando, en su forma infija.
        """
        return self.parse(command, posfix)[0]
    
    def to_posfix(self, command: str) -> str:
        """Convierte una expresión de su forma prefija a posfija.

        Retorna:
            Una representación en string de la expresión introducida en el
            comando, en su forma posfija.
        """
        stack = []
        prefix_expr = command.split()
        i = len(prefix_expr) - 1
        while  i >= 0:
            cur = prefix_expr[i]
            if self.is_operand(cur, True):
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(f'{op1} {op2} {cur}')
            elif self.is_operand(cur, False):
                op = stack.pop()
                stack.append(f'{op} {cur}')
            else:
                stack.append(cur)
            i -= 1
        return stack.pop()

    def is_operand(self, token: str, binary: bool) -> bool:
        """Determina si el token es un operando binario o unario.

        Retorna:
            True si el token es un operando según el caso, False en caso
            contrario.
        """
        return token in self.bin_operators if binary else token in self.un_operators
