"""Definiciones de reglas para el parser de BooleanEvaluator.
CI3641 - Lenguajes de Programación I
Pregunta 2

Christopher Gómez (c) 2022
"""
from .tokenrules import tokens

# -------- REGLAS DE PRECEDENCIA Y ASOCIATIVIDAD --------
precedence = (
    ('right', 'THEN'),
    ('left', 'AND', 'OR'),
    ('nonassoc', 'NOT'),
)

# -------- EXPRESIONES --------
# <expresion> -> <postfija1>
def p_instruccion(p):
    '''expresion : posfija1'''
    p[0] = p[1]


# -------- IMPLICACIÓN --------
# <posfija1> -> <posfija2> <posfija1> =>
def p_posfija1(p):
    '''posfija1 : posfija2 posfija1 THEN
        | posfija2'''
    if len(p) == 2:
        p[0] = p[1]
        return

    p2_str = p[1][0]
    p2_val = p[1][1]

    p1_str = p[2][0]
    p1_val = p[2][1]
    p[0] = (f'{p2_str} => {p1_str}', (not p2_val) or p1_val)

# -------- DISYUNCIÓN / CONJUNCIÓN --------
# <posfija2> -> <posfija2> <posfija3> &
#     | <posfija2> <posfija3> |
#     | <posfija3>
def p_posfija2(p):
    '''posfija2 : posfija2 posfija3 AND
        | posfija2 posfija3 OR
        | posfija3'''
    if len(p) == 2:
        p[0] = p[1]
        return

    p2_str = p[1][0]
    p2_val = p[1][1]

    p3_str = p[2][0]
    p3_val = p[2][1]

    if p[3] == '&':
        p0_val = p2_val and p3_val
    else:
        p0_val = p2_val or p3_val

    p[0] = (f'{p2_str} {p[3]} {p3_str}', p0_val)

# -------- NEGACIÓN --------
# <posfija3> -> <posfija3> ^
#     | <bool>
#     | <posfija>
def p_posfija3(p):
    '''posfija3 : posfija3 NOT
        | bool'''
    if len(p) == 2:
        p[0] = p[1]
        return

    p3_str = p[1][0]
    p3_val = p[1][1]

    p[0] = (f'^ {p3_str}', not p3_val)

# <posfija3> -> <posfija1>
def p_posfija3_reset(p):
    '''posfija3 : posfija1'''
    p1_str = p[1][0]
    p1_val = p[1][1]
    p[0] = (f'({p1_str})', p1_val)

# =========== EXPRESIONES TERMINALES ===========
# <bool> -> true | false
def p_bool(p):
    '''bool : TRUE
        | FALSE'''
    bool_str = p[1].lower()
    bool_val = True if bool_str == 'true' else False
    p[0] = (bool_str, bool_val)

# ======== ERRORES ============
def p_error(p):
    raise Exception()
