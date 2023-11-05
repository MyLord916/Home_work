def cesar_cript(message: str, n: int) -> str:
    alpha_ru_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alpha_ru_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alpha_en_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_en_lower = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for el in message:
        if el in alpha_ru_upper + alpha_ru_lower:
            if el.isupper():
                let = alpha_ru_upper.find(el)
                cur = alpha_ru_upper[(let + 32 + n) % 32]
                res += cur
            elif el.islower():
                let = alpha_ru_lower.find(el)
                cur = alpha_ru_lower[(let + 32 + n) % 32]
                res += cur
        elif el in alpha_en_upper + alpha_en_lower:
            if el.isupper():
                let = alpha_en_upper.find(el)
                cur = alpha_en_upper[(let + 26 + n) % 26]
                res += cur
            elif el.islower():
                let = alpha_en_lower.find(el)
                cur = alpha_en_lower[(let + 26 + n) % 26]
                res += cur
        else:
            res += el
    return res