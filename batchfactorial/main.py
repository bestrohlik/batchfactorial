import math
import sys

sys.set_int_max_str_digits(0)

def create_bf_code(number, title="file.bf"):
    # Spočítá faktoriál
    calculation = math.factorial(number)

    # Vytvoří jeden soubor
    with open(title, "w", encoding="utf-8") as f:
        f.write("!")
        f.write(str(calculation))
        f.write("!BF!")

# Použití:
create_bf_code(5)
