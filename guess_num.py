from random import randint


def state_poling():
    if state == 'start':
        rd_num = randint(1, set_num)
        print(rd_num)
        print(f'Загаданно число от 1 до {set_num}, попробуй отгадать')
        state = 'new_game'
        return
    elif state == 'new_game':
        if answer.isdigit and 1 < int(answer) < set_num:
            inp_num = int(answer)
            if inp_num < rd_num:
                attempt += 1
                print('Ваше число меньше загаданного, попробуйте еще разок')
                return
            elif inp_num > rd_num:
                attempt += 1
                print('Ваше число больше загаданного, попробуйте еще разок')
                return
            else:
                attempt += 1
                print(f'Вы угадали, поздравляем! Вы справились за {attempt} попыток(ки)')
                return
        else:
            print(f'А может быть все-таки введем целое число от 1 до {set_num}?')
            return


state = 'start'
set_num = 100
rd_num = None
attempt = 0

print('Добро пожаловать в числовую угадайку!\n')
print(state)
while True:
    answer = input()
    state_poling()

print('\nСпасибо, что играли в числовую угадайку. Еще увидимся...')
