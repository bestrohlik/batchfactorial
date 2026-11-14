import math
import sys
import os

sys.set_int_max_str_digits(0)

def create_bf_code(number, title="file.bf"):
    if not isinstance(number, int) or number < 0:
        raise ValueError("Number must be a non-negative integer!")

    if not title.endswith(".bf"):
        title += ".bf"

    calculation = math.factorial(number)

    # Absolutní cesta k souboru
    path = os.path.join(os.getcwd(), title)

    with open(path, "w", encoding="utf-8") as f:
        f.write(f"!{calculation}!BF!")
