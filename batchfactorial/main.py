import os
import math
import sys

sys.set_int_max_str_digits(0)

def create_bf_code(bf_code, nazev_souboru="soubor.bf"):
    calculation = math.factorial(bf_code)

    # Použijeme parametr nazev_souboru místo globální proměnné
    if not os.path.exists(nazev_souboru):
        open(nazev_souboru, "w").close()

    with open(nazev_souboru, "w", encoding="utf-8") as f:
        f.write("!")
        f.write(str(calculation))
        f.write("!BF!")

# --- Jak to teď můžeš používat: ---

# 1. Vytvoří výchozí "soubor.bf" (když druhý parametr vynecháš)
create_bf_code(5)

# 2. Vytvoří přesně ten soubor, který napíšeš
create_bf_code(5, "test.bf")
