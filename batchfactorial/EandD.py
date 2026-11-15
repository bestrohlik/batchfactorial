# Malá i velká písmena (české znaky včetně diakritiky)
LOWER = "aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž"
UPPER = LOWER.upper()

# Číslice a interpunkce (dostanou kódy až za písmeny)
DIGITS = "0123456789"
PUNCT = ".,!?-:;"

abc = list(LOWER) + list(UPPER) + list(DIGITS) + list(PUNCT)

# 00 = mezera, 01..99 = znaky (dvoumístné kódy => max. 99 znaků)
assert len(abc) <= 99, "Abeceda je příliš dlouhá pro dvoumístné kódy!"
encoded = [str(i).zfill(2) for i in range(1, len(abc) + 1)]

CHAR_TO_CODE = dict(zip(abc, encoded))
CODE_TO_CHAR = dict(zip(encoded, abc))


def encode_bf_code(text, wrap=True):
    result = []

    for char in text:
        if char == " ":
            result.append("00")
        elif char in CHAR_TO_CODE:
            result.append(CHAR_TO_CODE[char])
        # neznámé znaky (závorky, uvozovky, nové řádky...) se přeskočí

    code = "".join(result)
    return f"!{code}!BF!" if wrap else code


def decode_bf_code(code):
    # Odstranění BF obalu
    if code.startswith("!") and code.endswith("!BF!"):
        code = code[1:-4]

    if len(code) % 2 != 0:
        return "ERROR: Invalid BF code!"

    result = []

    for i in range(0, len(code), 2):
        number = code[i:i + 2]

        if number == "00":
            result.append(" ")
        elif number in CODE_TO_CHAR:
            result.append(CODE_TO_CHAR[number])
        else:
            return "ERROR: Unknown BF character!"

    return "".join(result)


if __name__ == "__main__":
    text = "Příliš žluťoučký kůň má 3 jablka, že?"
    kod = encode_bf_code(text)
    print(kod)
    print(decode_bf_code(kod))  # Příliš žluťoučký kůň má 3 jablka, že?
