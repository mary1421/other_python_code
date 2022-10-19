'''
const_upper_ru = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
const_lower_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
'''
first_txt = input().split() #вводим фразу и раскидываем слова по списку
last_txt = full = '' #для каждого слова и полной фразы


'''
for i in first_txt:
    if i in const_upper_ru:
        new_simb = const_upper_ru[(const_upper_ru.find(i) - 7) % 32]
        last_txt += new_simb
    elif i in const_lower_ru:
        new_simb = const_lower_ru[(const_lower_ru.find(i) - 7) % 32]
        last_txt += new_simb
    else:
        last_txt += i
print(last_txt)

for i in first_txt:
    if i in const_upper_ru:
        new_simb = const_upper_ru[(const_upper_ru.find(i) + 10) % 32]
        last_txt += new_simb
    elif i in const_lower_ru:
        new_simb = const_lower_ru[(const_lower_ru.find(i) + 10) % 32]
        last_txt += new_simb
    else:
        last_txt += i
print(last_txt)

for i in first_txt:
    if i.isalpha() == True and i.isupper() == True:
        ordup = ord(i)
        new_simb_up_n = (ordup - 65 + 17) % 26 + 65
        new_simb_up = chr(new_simb_up_n)
        last_txt += new_simb_up
    elif i.isalpha() == True:
        ordlow = ord(i)
        new_simb_low_n = (ordlow - 97 + 17) % 26 + 97
        new_simb_low = chr(new_simb_low_n)
        #new_simb = chr((ord(i) - 96 + 17) % 26 + 97)
        last_txt += new_simb_low
    else:
        last_txt += i

print(last_txt)

'''
for word in first_txt:
    if word.isalpha() == True:
        h = len(word)
    elif word[0].isalpha() != True and word[-1].isalpha() != True:
        h = len(word) - 2
    else:
        h = len(word) - 1
    for i in word:
        if i.isalpha() == True and i.isupper() == True: #Блок для заглавных букв
            ordup = ord(i)
            new_simb_up_n = (ordup - 65 + h) % 26 + 65
            new_simb_up = chr(new_simb_up_n)
            last_txt += new_simb_up
        elif i.isalpha() == True: #Блок для прописных букв
            ordlow = ord(i)
            new_simb_low_n = (ordlow - 97 + h) % 26 + 97
            new_simb_low = chr(new_simb_low_n)
            last_txt += new_simb_low
        else: #Блок для прочих символов
            last_txt += i
    full += last_txt + ' '
    last_txt = ''

print(full.rstrip())
