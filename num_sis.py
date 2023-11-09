def num_sis(num, inp, out):
    # Алфавиты кодировок 16 битной системы счисления
    alpha_in_16 = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    alpha_to_16 = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    # Если кодировка происходит из 10 битной системы счисления
    if inp == 10 and out != 10:
        res = ''
        while num >= out:
            cur = num % out
            if out == 16 and cur > 9:
                res += (alpha_in_16[cur])  # Если кодировка происходит в 16 бит
            else:
                res += (str(cur))
            num = num // out
        res += (str(num))
        res = res[::-1]
        if res.isdigit():
            res = int(res)
        return res
    # Если кодировка происходит в 10 бит
    elif inp != 10 and out == 10:
        res = 0
        if not str(num).isdigit():  # Если кодировка происходит из 16 бит
            num = str(num)
            for i in range(len(num)):
                if num[-1].isalpha():
                    cur_num = alpha_to_16[num[-1].upper()]
                    num = num[:-1]
                else:
                    cur_num = num[-1]
                    num = num[-1]
                res += int(cur_num) * inp ** i
        else:
            for i in range(len(str(num))):
                cur_num = num % 10
                res += cur_num * inp ** i
                num = num // 10
        return res


# Перевод из 2 бит в 10
result = num_sis(110101, 2, 10)
assert result == 53

# Перевод из 4 бит в 10
result = num_sis(3211, 4, 10)
assert result == 229

# Перевод из 8 бит в 10
result = num_sis(214, 8, 10)
assert result == 140

# Перевод из 16 бит в 10
result = num_sis('2AF', 16, 10)
assert result == 687

# Перевод из 10 бит в 2
result = num_sis(25, 10, 2)
assert result == 11001

# Перевод из 10 бит в 8
result = num_sis(125, 10, 8)
assert result == 175

# Перевод из 10 бит в 16
result = num_sis(428, 10, 16)
assert result == '1AC'
