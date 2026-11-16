# Vygenerujeme tisknutelné znaky
abc = [chr(i) for i in range(32, 127)] + [
    char for char in "áéěíóúůýžščřďťňÁÉĚÍÓÚŮÝŽŠČŘĎŤŇ" if char not in [chr(i) for i in range(32, 127)]
]

# 000 = mezera, 001 = nový řádek (\n), 002..999 = ostatní znaky
# Abychom se trefili do čísel, posuneme indexy o 2 (nebo si novou řádku nadefinujeme ručně)
CHAR_TO_CODE = {"\n": "001", " ": "000"}
CODE_TO_CHAR = {"001": "\n", "000": " "}

# Naplníme zbytek abecedy od kódu "002" dál
for idx, char in enumerate(abc, start=2):
    code = str(idx).zfill(3)
    CHAR_TO_CODE[char] = code
    CODE_TO_CHAR[code] = char


def encode_bf_code(text, wrap=True):
    result = []

    for char in text:
        if char in CHAR_TO_CODE:
            result.append(CHAR_TO_CODE[char])
        else:
            # Neznámé znaky raději přeskočíme, aby to nespadlo
            pass

    code = "".join(result)
    return f"!{code}!BF!" if wrap else code


def decode_bf_code(code):
    if code.startswith("!") and code.endswith("!BF!"):
        code = code[1:-4]

    if len(code) % 3 != 0:
        return "ERROR: Invalid BF code!"

    result = []

    for i in range(0, len(code), 3):
        number = code[i:i + 3]

        if number in CODE_TO_CHAR:
            result.append(CODE_TO_CHAR[number])
        else:
            return "ERROR: Unknown BF character!"

    return "".join(result)


if __name__ == "__main__":
    text = "První řádek\nDruhý řádek s mezerou a emoji 🚀"
    kod = encode_bf_code(text)
    print("Zakódováno:\n", kod)
    print("\nDekódováno:\n", decode_bf_code(kod))
