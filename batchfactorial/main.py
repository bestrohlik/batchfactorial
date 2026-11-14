import math
import sys

sys.set_int_max_str_digits(0)

def create_bf_code(cislo, nazev_souboru="soubor.bf"):
    # Spočítá faktoriál z čísla, které předáš do funkce
    calculation = math.factorial(cislo)

    with open(nazev_souboru, "w", encoding="utf-8") as f:
        f.write("!")
        f.write(str(calculation))
        f.write("!BF!")

# --- Jak to pak používáš: ---

# 1. Spočítá faktoriál z 5 a uloží do "soubor.bf"
create_bf_code(5)

# 2. Spočítá faktoriál z 10 a uloží do "test.bf"
create_bf_code(10, "test.bf")

# 3. Nebo si můžeš nechat číslo zadat od uživatele:
# uzivatelske_cislo = int(input("Zadej číslo: "))
# create_bf_code(uzivatelske_cislo, "vysledek.bf")
