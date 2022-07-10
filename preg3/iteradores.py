from ast import arg
from sys import argv

def ins(e, ls):
    yield [e, *ls]
    if ls:
        for i in ins(e, ls[1:]):
            yield [ls[0], *i]

def misterio(ls):
    if ls:
        for m in misterio(ls[1:]):
            # print(f"yield m: {m}")
            for i in ins(ls[0], m):
                # print(f"yield i: {m}")
                yield i
    else:
        yield []

def main():
    if len(argv) != 2:
        print(f"Uso: python3 {argv[0]} <n>")
        return
    
    try:
        n = int(argv[1])
    except:
        print("El argumento n debe ser un entero no negativo")
        return

    print(f"bienParentizadas({n}):")
    for i, expr in enumerate(bienParentizadas(n)):
        print(expr, end="\t")
        if (i + 1) % 3 == 0:
            print()
    print()

def bienParentizadas(n: int) -> str:
    ''' Iterador que genera el conjunto de todas las expresiones bien parentizadas
    con n pares de paréntesis.
    '''
    # Se mantiene un conjunto con las expresiones bien parentizadas
    # que se han hallado hasta el momento.
    expr_set = set()
    
    # Caso base: Ningún par de paréntesis
    if n == 0:
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
    # for i in ins(0, [1, 2, 3]):
    #     print("ins:", i)

    # for m in misterio([1, 2, 3]):
    #     print("misterio:", m)

    # count = 0
    # for par in bienParentizadas(5):
    #     count += 1
    #     print("bienParentizadas:", par)
    # print(count)
    main()