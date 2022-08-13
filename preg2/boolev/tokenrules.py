"""Definiciones de reglas para el tokenizer de BooleanEvaluator.
CI3641 - Lenguajes de Programación I
Pregunta 2

Christopher Gómez (c) 2022
"""
# =========== DEFINICIONES DE TOKENS ===========
tokens = ['NOT','AND', 'OR', 'THEN', 'TRUE', 'FALSE']

# Se debe ignorar todo tipo de espacio en blanco
t_ignore = r' '

# Expresiones regulares para los tokens
t_TRUE   = r'true'
t_FALSE  = r'false'
t_NOT    = r'\^'
t_AND    = r'&'
t_OR     = r'\|'
t_THEN   = r'=>'

# Manejo de caracteres ilegales
def t_error(t):
    t.type = 'IllegalChar'
    t.value = t.value[0]

    # Salta el caracter ilegal
    t.lexer.skip(1)
    return t