from random import *

#варианты используемых символов
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = "'!#$%&*+-=?@^_"
exx = 'il1Lo0O'

allow = '' #алфавит для пароля

#формируем требования к паролю
print('Введите требуемое количество паролей')
count = int(input())
print('Введите требуемую длинну пароля (Да/Нет)')
l = int(input())
print('Включать цифры? (Да/Нет)')
if input() == 'Да':
    allow += digits
print('Включать прописные буквы? (Да/Нет)')
if input() == 'Да':
    allow += lowercase_letters
print('Включать заглавные буквы? (Да/Нет)')
if input() == 'Да':
    allow += uppercase_letters
print('Включать знаки пунктуации? (Да/Нет)')
if input() == 'Да':
    allow += punctuation
print('Исключать неоднозначные символы? (Да/Нет)')
if input() == 'Да':
    for i in exx:
        if i in allow:
            allow = allow.replace(i, '')

#генерируем пароль, исходя из условий
def generate_password(length, chars):
    one_pass = ''
    for _ in range(length):
        one_pass += choice(chars)
    return one_pass

#формируем список паролей
passes = []
for _ in range(count):
    passes.append(generate_password(l, allow))

print('Пароли сгенерированы:')
print(*passes, sep='\n')
