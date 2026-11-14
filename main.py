import os
import math
import sys

sys.set_int_max_str_digits(0)

file = "soubor.bf"

def create_bf_code(bf_code):
    calculation = math.factorial(bf_code)

    if not os.path.exists(file):
        open(file, "w").close()

    with open(file, "w", encoding="utf-8") as f:
        f.write("!")
        f.write(str(calculation))
        f.write("!BF!")