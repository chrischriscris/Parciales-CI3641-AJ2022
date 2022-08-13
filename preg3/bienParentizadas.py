"""Generador de expresiones bien parentizadas con n pares de paréntesis.
CI3641 - Lenguajes de Programación I
Pregunta 3

Christopher Gómez (c) 2022
"""
from sys import argv

def main():
    '''Entry-point de bienParentizadas.py, imprime todas las posibles
    expresiones bien parentetizadas con n pares de paréntesis y su cuenta.
    Recibe n por línea de comandos.
    '''
    if len(argv) != 2:
        print(f"Uso: python3 {argv[0]} <n>")
        return
    
    try:
        n = int(argv[1])
    except:
        print(f'"{argv[1]}" no es un número entero')
        return

    print(f"bienParentizadas({n})")
    for i, expr in enumerate(bienParentizadas(n)):
        print(expr, end='    ')
        if (i+1) % 3 == 0:
            print()

    print(f"\nHay un total de {i+1} expresiones bien parentizadas.")

def bienParentizadas(n: int) -> str:
    ''' Iterador que genera el conjunto de todas las expresiones bien parentizadas
    con n pares de paréntesis.
    '''
    # Se mantiene un conjunto con las expresiones bien parentizadas
    # que se han hallado hasta el momento.
    expr_set = set()
    
    # Caso base: Ningún par de paréntesis (o menos?)
    if n <= 0:
        expr_set.add("")
        yield ""
        return
    
    # Caso recursivo: A partir de las expresiones bien parentizadas con un
    # par menos de paréntesis
    for expr in bienParentizadas(n - 1):
        # La misma expresión con un par de paréntesis a la derecha
        expr1 = f"{expr}()"
        if expr1 not in expr_set:
            expr_set.add(expr1)
            yield f"{expr}()"

        # Análogamente a la izquierda
        expr2 = f"(){expr}"
        if expr2 not in expr_set:
            expr_set.add(expr2)
            yield expr2

        # La misma expresión encerrada entre paréntesis
        expr3 = f"({expr})"
        if expr3 not in expr_set:
            expr_set.add(expr3)
            yield expr3

if __name__ == "__main__":
    main()