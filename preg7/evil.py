from sys import argv
from flint import *
from math import frexp
from numpy import floor

print(
    fmpz.fib_ui(
        floor(
            fmpz.bell_number(int(argv[1])+1).bit_length() - 1
        )
    +1
    )
)
