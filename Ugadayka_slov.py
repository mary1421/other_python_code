from random import *

word_list = ["Булочка", "Кошка", "Пылесос", "Колобок", "Банан", "Капуста", "Зайка", "Огород"]

def get_word():
    return choice(word_list)


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

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print('Давайте играть в угадайку слов!')
    print('Пока картина такая')
    print(display_hangman(tries))
    print('Наше слово ' + word_completion)
    while guessed == False or tries >= 1:
        print('Введите букву или слово целиком')
        user_in = input().upper()
        if user_in.isalpha() == False:
            print('Используйте только буквы')
        else:
            if len(user_in) == 1:
                if user_in in guessed_letters:
                    print('Эта буква уже называлась')
                else:
                    guessed_letters.append(user_in)
                    if user_in in word:
                        for i in range(len(word)):
                            if user_in == word[i]:
                                word_completion = word_completion[:i] + user_in.upper() + word_completion[i + 1:]
                        print('Угадали' + word_completion)
                    else:
                        print('Такой буквы нет, попытка исчерпана')
                        tries -= 1
                        print(display_hangman(tries))
                        if tries == 0:
                            print('Вы исчерпали все попытки, загаданное слово ' + word.upper())
                            print('Сыграем ещё? (Да/Нет)')
                            if input() == 'Да':
                                play(get_word().upper())
                            else:
                                guessed = True
                                print('Пока-пока!')
            else:
                if user_in == word:
                    print('Поздравляем, вы угадали слово! Вы победили!')
                    tries = 0
                    print('Сыграем ещё? (Да/Нет)')
                    if input() == 'Да':
                        play(get_word())
                    else:
                        guessed = True
                        print('Пока-пока!')
                else:
                    if user_in in guessed_words:
                        print('Это слово уже называлось')
                    else:
                        print('Слово неверно, попытка исчерпана!')
                        tries -= 1
                        print(display_hangman(tries))
                        if tries == 0:
                            print('Вы исчерпали все попытки, загаданное слово ' + word.upper())
                            print('Сыграем ещё? (Да/Нет)')
                            if input() == 'Да':
                                play(get_word().upper())
                            else:
                                guessed = True
                                print('Пока-пока!')

play(get_word().upper())

