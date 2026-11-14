abc = list("aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž")
encoded = [str(i).zfill(2) for i in range(1, 41)]

def encode_bf_code(text):
    result = []

    for char in text.upper():
        if char in abc:
            result.append(encoded[abc.index(char)])
        elif char == " ":
            result.append("00")

    return "".join(result)


def decode_bf_code(code):
    result = []

    # Odstranění BF obalu
    if code.startswith("!") and code.endswith("!BF!"):
        code = code[1:-4]

    if len(code) % 2 != 0:
        return "ERROR: Invalid BF code!"

    for i in range(0, len(code), 2):
        number = code[i:i+2]

        if number == "00":
            result.append(" ")
        elif number in encoded:
            result.append(abc[encoded.index(number)])
        else:
            return "ERROR: Unknown BF character!"

    return "".join(result)
