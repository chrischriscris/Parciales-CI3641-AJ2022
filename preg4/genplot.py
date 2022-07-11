"""Script que genera gráficas de tiempos de ejecución de las funciones de la
pregunta 4.

CI3641 - Lenguajes de Programación I
Pregunta 4

Christopher Gómez (c) 2022
"""
from sys import argv
from matplotlib import pyplot as plt

def main():
    n = [i for i in range(131)]
    rec = []
    tailrec = []
    it = []
    with open(argv[1], "r") as fi:
        for i, line in enumerate(fi):
            if line.startswith("f_54_rec"):
                times = rec
                continue
            elif line.startswith("f_54_tailrec"):
                times = tailrec
                continue
            elif line.startswith("f_54_it"):
                times = it
                continue
            elif not line:
                continue

            line = line.split(":")[1]
            if "ns" in line:
                times.append(float(line[:-3]) / 1000)
            elif "µs" in line:
                times.append(float(line[:-3]))
            elif "ms" in line:
                times.append(float(line[:-3]) * 1000)
            elif "s" in line:
                times.append(float(line[:-2]) * 1000000)

    # Gráfica para n=1..130
    plt.figure()
    plt.plot(n, rec, n, tailrec, n, it)
    plt.title("tiempos de ejecución de f_54")
    plt.legend(["f_54_rec", "f_54_tailrec", "f_54_it"])
    plt.xlabel("n")
    plt.ylabel("tiempo (µs)")
    plt.savefig(f"{argv[1]}1.png")

    # Gráficas para n=1..40
    n = n[:40]
    rec = rec[:40]
    tailrec = tailrec[:40]
    it = it[:40]
    plt.figure()
    plt.plot(n, rec, n, tailrec, n, it)
    plt.title("tiempos de ejecución de f_54")
    plt.legend(["f_54_rec", "f_54_tailrec", "f_54_it"])
    plt.xlabel("n")
    plt.ylabel("tiempo (µs)")
    plt.savefig(f"{argv[1]}2.png")

if __name__ == "__main__":
    main()