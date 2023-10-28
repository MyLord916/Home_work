import random


def user_input():  # Принимаем ввод пользователя
    answer = input()
    if answer.isdigit() and 1 <= int(answer) <= set_num:  # Если введено число переводим в int
        return int(answer)
    elif answer.isalpha() and answer.upper() == 'S':  # Дальнейший вывод в настройки
        return 'S'
    else:
        print(f'А может быть все-таки введем целое число от 1 до {set_num}?')  # Защита от неправильного ввода
        return user_input()


def start_block(n):
    print(f'Загаданно число от 1 до {n}, попробуй отгадать')  # Загадываем число
    rd_num = random.randint(1, n)
    print(rd_num)  # Подсказка загаданного числа для тестов
    return rd_num


def comparison(answer, n=0):  # Проверяем ответ и считаем попытки
    attempt = n

    if answer < rd_num:
        attempt += 1
        print('Ваше число меньше загаданного, попробуйте еще разок')
        return comparison(user_input(), attempt)
    elif answer > rd_num:
        attempt += 1
        print('Ваше число больше загаданного, попробуйте еще разок')
        return comparison(user_input(), attempt)
    else:
        attempt += 1
        print(f'Вы угадали, поздравляем! Вы справились за {attempt} попыток(ки)')
        return


def new_game(set=True):  # В конце игры предлагаем еще партейку
    if set:
        print('\nХотите сыграть заново? (Y / N)')
    answer = input()
    if answer.upper() == 'Y':
        return True
    elif answer.upper() == 'N':
        return False
    elif answer.upper() == 'S':  # Выход в настройки
        return 'S'
    else:
        print("Нужен ответ только 'Y' или 'N'")  # Защита от неправильного ввода
        return new_game(False)


def setting(set=True):  # Настройки по диапазону случвйного числа
    if set:
        print('Можете настроить парраметры игры, укажите предел загаданного числа:', end=' ')
    answer = input()
    if answer.isdigit() and int(answer) > 1:
        return int(answer)
    else:
        print('Нужно указать целое число больше 1')
        return setting(False)


set_num = 100  # Стартовое значение диапазона
rd_num = None

print('Добро пожаловать в числовую угадайку!\n')

loop = True
while loop:
    rd_num = start_block(set_num)  # Загадываем число через стартовый блок с параметром стартового значения
    inp = user_input()
    if inp != 'S':  # проверка на отсутствие входа в настройки
        comparison(inp)
        loop = new_game()  # Перезапускаем цикл или прерываем его через вопрос о новой игре
        if loop == 'S':
            set_num = setting()  # Выход в настройки через концовку игры
    else:
        set_num = setting()  # Выход в настройки в сердине или начале игры

print('\nСпасибо, что играли в числовую угадайку. Еще увидимся...')
