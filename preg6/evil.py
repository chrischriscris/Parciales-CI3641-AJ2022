from sys import argv
from sympy import*
print(fibonacci(floor(log(bell(int(argv[1])+1),2))+1))