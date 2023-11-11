from random import choice

# Список случайных слов
word_list = [
    'биоразнообразие',
    'трехзубость',
    'лигаментит',
    'сферофизин',
    'кегичевец',
    'пазовость',
    'пеладофоб',
    'неудобье',
    'попойка',
    'отруби'
]


# Получение случайного слова
def get_word():
    global word_list
    res = choice(word_list)
    return res.upper()


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


# Отображение текущего состояния
def play_state():
    print(display_hangman(tries))
    print(word_completion)
    return


def play():
    global word, word_completion, guessed_words, guessed_letters, tries, state
    if state == 'start':  # Блок приветствия
        print('Давайте играть в угадайку слов!\n')

        play_state()

        print(word)  # Подсказка для отладки

        state = 'game'
        return
    elif state == 'game':  # Игровой блок
        if tries != 0:  # Считаем оставшиеся попытки
            answer = input().upper()
            if answer.isalpha():  # Проверка ввода на отсутствие цифр, пустой строки и символов пунктуации
                if len(answer) <= len(word):  # Проверка длинны введенного слова
                    if len(answer) == 1:  # Обработка побуквенного отгадывания слова
                        if answer not in guessed_letters:
                            if answer in word:
                                word_completion = list(word_completion)
                                for i in range(len(word)):
                                    if word[i] == answer:
                                        word_completion[i] = answer
                                word_completion = ''.join(word_completion)
                                guessed_letters.append(answer)
                                play_state()
                                return
                            else:
                                tries -= 1
                                guessed_letters.append(answer)
                                play_state()
                                return
                        else:
                            print('\nЭта буква уже использовалась, попробуй другую\n')
                            return
                    else:
                        if len(answer) <= len(word):  # Обработка отгадывания слова целиком
                            if answer not in guessed_words:
                                if answer == word:
                                    state = 'win'
                                    return
                                else:
                                    tries -= 1
                                    guessed_words.append(answer)
                                    play_state()
                                    return
                            else:
                                print(
                                    '\nЭто слово уже использовалась, попробуй другое\n')
                                return
                else:
                    print('В загаданном слове даже нет столько букв')
                    return
            else:
                print('\nНужно ввести букву или слово целиком\n')
                return
        else:
            state = 'defeat'
            return
    elif state == 'defeat':  # Блок поражения
        print(f"\nИгра окончена, вы не угадали слово '{word}'\n")
        print('\nЖелаете сыграть еще раз?\n')
        state = 'new_game'
    elif state == 'win':  # Блок выигрыша
        print(f"\nПоздравляем, вы угадали слово '{word}'! Вы победили!\n")
        print('\nЖелаете сыграть еще раз?\n')
        state = 'new_game'
        return
    elif state == 'new_game':  # Блок опроса новой игры
        answer = input().upper()
        if answer == 'Y' or answer == 'Н':
            tries = 6
            word = get_word()
            word_completion = '_' * len(word)
            state = 'start'
            return
        elif answer == 'N' or answer == 'Т':
            state = 'exit'
            return
        else:
            print("\nНужен ответ только 'Y' или 'N'\n")
            return


state = 'start'  # Статус игрового блока
word = get_word()  # Случайное число
word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
guessed_letters = []  # список уже названных букв
guessed_words = []  # список уже названных слов
tries = 6  # количество попыток

while state != 'exit':  # Цикл игры
    play()
