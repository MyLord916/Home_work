import random

digits = '0123456789'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
punctuation = '!#$%&*+-=?@^_'
chars = ''

def pass_generate(cp=1, lop=12, dig=True, ABC=True, abc=True, sim=True, ord=True):
    global digits, uppercase_letters, lowercase_letters, punctuation, chars
    keys = ''
    if dig:
        keys += digits
    if ABC:
        keys += uppercase_letters
    if abc:
        keys += lowercase_letters
    if sim:
        keys += punctuation
    if ord:
        for i in 'il1Lo0O':
            keys = keys.replace(i, '')
    keys = list(keys)
    random.shuffle(keys)
    keys = ''.join(keys)

    for i in range(cp):
        for _ in range(lop):
            chars += random.choice(keys)
        print(f'{i+1}: {chars}')
        chars = ''

state = 'start_survey'
message = ''

def poll_state():
    global state, gen_setup, message

    #   Начало опроса

    if state == 'start_survey':
        state = 'count_pass'
        print('\nУкажите необходимое кол-во паролей для генерации:\n')
        return

    #   Кол-во паролей

    elif state == 'count_pass':
        answer = input()
        if answer.isdigit() and int(answer) > 1:
            gen_setup[0] = int(answer)
            print('\nУкажите желаеиую длинну пароля:\n')
            state = 'len_one_pass'
            return
        else:
            print('\nНужно указать целое число больше 1\n')
            return

    #   Длинна паролей

    elif state == 'len_one_pass':
        answer = input()
        if answer.isdigit() and int(answer) > 1:
            gen_setup[1] = int(answer)
            print('\nИспользовать при генерации цифры " 0123456789 "\n')
            state = 'digit_in_pass'
            return
        else:
            print('\nНужно указать целое число больше 1\n')
            return

    #   Использование цифр

    elif state == 'digit_in_pass':
        message = '\nИспользовать при генерации прописные буквы\n" ABCDEFGHIJKLMNOPQRSTUVWXYZ " ?\n'
        answer = input()
        if answer.upper() == 'Y':
            gen_setup[2] = True
            print(message)
            state = 'ABC_in_pass'
            return
        elif answer.upper() == 'N':
            gen_setup[2] = False
            state = 'ABC_in_pass'
            print(message)
            return
        else:
            print("\nНужен ответ только 'Y' или 'N'\n")
            return

    #   Использование заглавных букв

    elif state == 'ABC_in_pass':
        message = '\nИспользовать при генерации строчные буквы\n" abcdefghijklmnopqrstuvwxyz " ?\n'
        answer = input()
        if answer.upper() == 'Y':
            gen_setup[3] = True
            print(message)
            state = 'abc_in_pass'
            return
        elif answer.upper() == 'N':
            gen_setup[3] = False
            state = 'abc_in_pass'
            print(message)
            return
        else:
            print("\nНужен ответ только 'Y' или 'N'\n")
            return

    #   Использование строчных букв

    elif state == 'abc_in_pass':
        message = '\nИспользовать при генерации специальные символы\n" !#$%&*+-=?@^_? " ?\n'
        answer = input()
        if answer.upper() == 'Y':
            gen_setup[4] = True
            print(message)
            state = 'sim_in_pass'
            return
        elif answer.upper() == 'N':
            gen_setup[4] = False
            state = 'sim_in_pass'
            print(message)
            return
        else:
            print("\nНужен ответ только 'Y' или 'N'\n")
            return

    #   Использование специальных символов

    elif state == 'sim_in_pass':
        message = '\nИсключить из генерации неоднозначные символы\n" il1Lo0O " ?\n'
        answer = input()
        if answer.upper() == 'Y':
            gen_setup[5] = True
            print(message)
            state = 'ord_sim_not'
            return
        elif answer.upper() == 'N':
            gen_setup[5] = False
            state = 'ord_sim_not'
            print(message)
            return
        else:
            print("\nНужен ответ только 'Y' или 'N'\n")
            return

    # Исключение неоднозначных символов

    elif state == 'ord_sim_not':
        message = '\nСгенерированные пароли:\n'
        answer = input()
        if answer.upper() == 'Y':
            gen_setup[6] = False
            print(message)
            state = 'exit'
            return
        elif answer.upper() == 'N':
            gen_setup[6] = True
            state = 'exit'
            print(message)
            return
        else:
            print("\nНужен ответ только 'Y' или 'N'\n")
            return

gen_setup = [1, 12, True, True, True, True, True]

while state != 'exit':
    poll_state()

pass_generate(gen_setup[0], gen_setup[1], gen_setup[2], gen_setup[3],
              gen_setup[4], gen_setup[5], gen_setup[6])