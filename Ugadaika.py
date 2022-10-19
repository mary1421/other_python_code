import sys
from random import *

n = randint(1, 100)
print('Добро пожаловать в числовую угадайку, введите число от 1 до 100')


def is_valid(h):  # функция валидации
    if int(h) > 100 or int(h) < 1:
        return False
    return True


p = input()  # Пользователь вводит число
count = 1  # Запускаем счетчик

# Валидация
flag = False
while flag == False:
    flag = True
    if is_valid(p) == False:
        flag = False
        print('А может быть все-таки введем целое число от 1 до 100?')
        p = input()
        count += 1
    else:
        p = int(p)

# Начинаем угадывать
while n != p:
    if p > n:
        print('Ваше число больше загаданного, попробуйте еще разок')
        p = int(input())
        count += 1
    else:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        p = int(input())
        count += 1
if n == p:
    print('Вы угадали, поздравляем!')
print('Спасибо, что играли в числовую угадайку. Вы использовали ' + str(count) + ' попыток. Еще увидимся...')
