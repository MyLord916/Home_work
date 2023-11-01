from random import randint


def state_poling():
    global state, rd_num, attempt, set_num
    if state == 'start':
        rd_num = randint(1, set_num)
        print(rd_num)
        print(f'Загаданно число от 1 до {set_num}, попробуй отгадать\n')
        state = 'game'
        return
    elif state == 'game':
        answer = input()
        if answer.isdigit() and 1 <= int(answer) <= set_num:
            inp_num = int(answer)
            if inp_num < rd_num:
                attempt += 1
                print('\nВаше число меньше загаданного, попробуйте еще разок\n')
                return
            elif inp_num > rd_num:
                attempt += 1
                print('\nВаше число больше загаданного, попробуйте еще разок\n')
                return
            else:
                attempt += 1
                print(f'\nВы угадали, поздравляем! Вы справились за {attempt} попыток(ки)\n')
                state = 'new_game'
                print('\nХотите сыграть заново? (Y / N)\n')
                return
        elif answer.upper() == 'S':
            print('Можете настроить парраметры игры, укажите предел загаданного числа:', end=' ')
            state = 'settings'
            return
        else:
            print(f'\nА может быть все-таки введем целое число от 1 до {set_num}?\n')
            return
    elif state == 'new_game':
        answer = input()
        if answer.upper() == 'Y':
            state = 'start'
            attempt = 0
            return
        elif answer.upper() == 'N':
            state = 'exit'
            return
        elif answer.upper() == 'S':
            print('Можете настроить парраметры игры, укажите предел загаданного числа:', end=' ')
            state = 'settings'
            return
        else:
            print("\nНужен ответ только 'Y' или 'N'\n")
            return
    elif state == 'settings':
        answer = input()
        if answer.isdigit() and int(answer) > 1:
            set_num = int(answer)
            state = 'start'
            attempt = 0
            return
        else:
            print('Нужно указать целое число больше 1')
            return


state = 'start'
set_num = 100
rd_num = None
attempt = 0

print('Добро пожаловать в числовую угадайку!\n')
print(state)
while state != 'exit':
    state_poling()
print('\nСпасибо, что играли в числовую угадайку. Еще увидимся...')
