uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


'''
d = dig = input()
ten = k = 0


for i in dig:
    if i.isalpha() == True:
        i = uppercase_letters.find(i) + 10
    r = int(i) * (16 ** (len(dig) - 1 - k))
    k += 1
    ten += r


d = dig = int(input())
fin = ''

# для перевода в 16

while d >= 16:
    c = d % 16
    d = d // 16
    if c > 9:
        cs = uppercase_letters[c - 10]
    else:
        cs = str(c)
    fin += cs
fin += str(d)
print(fin[::-1])

# для перевода в 2
while d >= 2:
    c = d % 2
    d = d // 2
    fin += str(c)
fin += str(d)
print(fin[::-1])

print(bin(d)[2:])
print(oct(d)[2:])
print(hex(d)[2:].upper())



a, b = input(), input()
for i in b:
    if a.count(i) != b.count(i):
        print(i)
        a = b
    elif i not in a:
        print(i)
        a = b
'''

s = [int(i) for i in input().split()]
f = sorted(s)
for i in s:
    if s.count(i) == 5:
        print('Шулер')
        break
    if f == [2, 3, 4, 5, 6]  or f == [3, 4, 5, 6 , 7] or  f == [4, 5, 6 , 7, 8] or f == [5, 6, 7, 8, 9] or f == [6, 7, 8, 9, 10]  or f == [7, 8, 9, 10, 11] or f == [8, 9, 10, 11, 12] or f == [9, 10, 11, 12, 13]:
        print('Стрит')
        break
    elif s.count(i) == 4:
        print('Каре')
        break
    elif s.count(i) == 3:
        for h in range(3):
            s.remove(i)
        if s[0] == s[1]:
            print('Фулл Хаус')
            break
        else:
            print('Сет')
            break
    elif s.count(i) == 2:
        for h in range(2):
            s.remove(i)
        if s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
            print('Две пары')
            break
        else:
            print('Пара')
            break
    else:
        print('Старшая карта')
        break
