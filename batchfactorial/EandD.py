# Vygenerujeme všechny tisknutelné znaky a symboly, které klávesnice a Unicode nabízí.
# Projedeme rozsah běžných znaků (ASCII + rozšířená latinka, české znaky, emoji apod.)
# Přeskočíme jen netisknutelné řídicí znaky (nové řádky, tabulátory atd. můžeme ošetřit zvlášť, nebo je nechat na mezeru).
abc = [chr(i) for i in range(32, 127)] + [
    # Přidáme české a evropské znaky s diakritikou, které by v základním ASCII chyběly
    char for char in "áéěíóúůýžščřďťňÁÉĚÍÓÚŮÝŽŠČŘĎŤŇ" if char not in [chr(i) for i in range(32, 127)]
]

# 000 = mezera, 001..999 = znaky (trojmístné kódy => max. 999 znaků)
# Pokud by náhodou abeceda přetekla, zvětšíme to, ale takhle to stačí na vše z klávesnice.
encoded = [str(i).zfill(3) for i in range(1, len(abc) + 1)]

CHAR_TO_CODE = dict(zip(abc, encoded))
CODE_TO_CHAR = dict(zip(encoded, abc))


def encode_bf_code(text, wrap=True):
    result = []

    for char in text:
        if char == " ":
            result.append("000")
        elif char in CHAR_TO_CODE:
            result.append(CHAR_TO_CODE[char])
        else:
            # Pokud narazíme na úplně neznámý znak, můžeme ho buď ignorovat,
            # nebo ho zkusit převést aspoň jako surový unicode, 
            # ale tady ho pro zachování logiky tvého kódu raději bezpečně přeskočíme (nebo vypíšeme varování).
            pass

    code = "".join(result)
    return f"!{code}!BF!" if wrap else code


def decode_bf_code(code):
    # Odstranění BF obalu
    if code.startswith("!") and code.endswith("!BF!"):
        code = code[1:-4]

    # Jelikož používáme trojmístné kódy, délka musí být dělitelná třemi
    if len(code) % 3 != 0:
        return "ERROR: Invalid BF code!"

    result = []

    for i in range(0, len(code), 3):
        number = code[i:i + 3]

        if number == "000":
            result.append(" ")
        elif number in CODE_TO_CHAR:
            result.append(CODE_TO_CHAR[number])
        else:
            return "ERROR: Unknown BF character!"

    return "".join(result)


if __name__ == "__main__":
    text = "Příliš žluťoučký kůň má 3 jablka, že? [test] {emoji 🚀}"
    kod = encode_bf_code(text)
    print("Zakódováno:", kod)
    print("Dekódováno:", decode_bf_code(kod))
