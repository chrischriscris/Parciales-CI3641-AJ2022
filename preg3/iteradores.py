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

def bienParentizadas(n):
    print(f"bienParentizadas({n})")
    if n == 0:
        yield ""
        return
    else:
        for i in bienParentizadas(n - 1):
            yield f"{i}()"
            yield f"(){i}"
            yield f"({i})"

if __name__ == "__main__":
    for i in ins(0, [1, 2, 3]):
        print("ins:", i)

    for m in misterio([1, 2, 3]):
        print("misterio:", m)

    for par in bienParentizadas(3):
        print("bienParentizadas:", par)