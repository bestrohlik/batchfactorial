import os
import math
import sys

sys.set_int_max_str_digits(0)

def create_bf_code(bf_code, nazev_souboru="soubor.bf"):
    calculation = math.factorial(bf_code)

    # Režim "w" automaticky vytvoří soubor, pokud neexistuje, 
    # a přepíše ho, pokud už existuje. Žádný další soubor nevznikne.
    with open(nazev_souboru, "w", encoding="utf-8") as f:
        f.write("!")
        f.write(str(calculation))
        f.write("!BF!")
