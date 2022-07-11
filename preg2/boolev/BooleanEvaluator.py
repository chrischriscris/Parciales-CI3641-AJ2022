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
    """
    def __init__(self):
        # No se imprime ningún mensaje que pueda generar ply
        self.lex = lex.lex(module=tokenrules)
        self.parser = yacc.yacc(module=grammar)

    def parse(self, command: str) -> Tuple[str, bool]:
        """Llama al parser de BooleanEvaluator.

        Retorna:
            Una tupla (string infija, evaluación) con el resultado del parsing.
        """
        try:
            return self.parser.parse(command, lexer=self.lex)
        except:
            return "Expresión inválida"

    def evaluate(self, command: str) -> str:
        """Evalúa la expresión dada.
        
        Retorna:
            Una representación en string del resultado de la evaluación.
        """
        return str(self.parse(command)[1]).lower()

    def show(self, command: str) -> str:
        """Convierte la expresión a su forma infija.

        Retorna:
            Una representación en string de la expresión introducida en el
            comando, en su forma infija.
        """
        return self.parse(command)[0]
