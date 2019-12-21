"""
В какой-то момент в Институте биоинформатики биологи перестали понимать,
что говорят информатики: они говорили каким-то странным набором звуков.

В какой-то момент один из биологов раскрыл секрет информатиков: они
использовали при общении подстановочный шифр, т.е. заменяли каждый символ
исходного сообщения на соответствующий ему другой символ. Биологи раздобыли
ключ к шифру и теперь нуждаются в помощи:

Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
Программа принимает на вход две строки одинаковой длины, на первой строке
записаны символы исходного алфавита, на второй строке — символы конечного
алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом,
и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре,
b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра.
Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac


Sample Input 1:
abcd
*d%#
abacabadaba
#*%*d*%

Sample Output 1:
*d*%*d*#*d*
dacabac


Sample Input 2:
dcba
badc
dcba
badc

Sample Output 2:
badc
dcba


"""
sourceAlf =  [str(i) for i in input()]
cryptAlf = [str(i) for i in input()]
myStrForCrypr =  input()
myStrForDecrypr =  input()

dictCrypt = dict(zip(sourceAlf, cryptAlf))

resCrypt = ''
for s in myStrForCrypr:
    for  key, value in dictCrypt.items():
        if s == key:
            resCrypt += str(value)

print(resCrypt)

resDecrypt = ''
for s in myStrForDecrypr:
    for  key, value in dictCrypt.items():
        if s == value:
            resDecrypt += str(key)

print(resDecrypt)

'''
===========================================================
codeKey = list(input())
decodeKey = list(input())
codeIt = input()
decodeIt = input()

shifrCode = dict(zip(codeKey, decodeKey))
shifrDecode = dict(zip(decodeKey, codeKey))

stIn = ""
stOut = ""

for ch in codeIt:
    for k, v in shifrCode.items():
        if ch == k:
            stIn += v

for ch in decodeIt:
    for k, v in shifrDecode.items():
        if ch == k:
            stOut += v

print(stIn)
print(stOut)
===========================================================
codeKey = input()
decodeKey = input()
codeIt = input()
decodeIt = input()

shifrCode = dict()
shifrDecode = dict()

stIn = ""
stOut = ""

for i in range(len(codeKey)):
    shifrCode.update({codeKey[i]: decodeKey[i]})
    shifrDecode.update({decodeKey[i]: codeKey[i]})

for ch in codeIt:
    for k, v in shifrCode.items():
        if ch == k:
            stIn += v

for ch in decodeIt:
    for k, v in shifrDecode.items():
        if ch == k:
            stOut += v

print(stIn)
print(stOut)
===========================================================
a,b,c,d=input(),input(),input(),input()
print(''.join(b[a.index(i)] for i in c))
print(''.join(a[b.index(i)] for i in d))
===========================================================
source, dest = input(), input()
decoded = input()
encoded = input()

print(decoded.translate(str.maketrans(source, dest)))
print(encoded.translate(str.maketrans(dest, source)))
===========================================================
# Считываем 4 строки в цикле
original, coding, first_string, second_string = (input() for i in range(4))
# По индексу символа из оригинала берём символ на замену из кодировки,
# для каждого символа из строки, которую нужно закодировать
print(*[coding[original.find(symbol)] for symbol in first_string], sep='')
# Аналогично, только наоборот :D
print(*[original[coding.find(symbol)] for symbol in second_string], sep='')
===========================================================
a1=input()
a2=input()
print(''.join([a2[a1.find(s)] for s in input()]))
print(''.join([a1[a2.find(s)] for s in input()]))
===========================================================
a, b, c, d = (input() for i in range(4))
print(''.join(dict(zip(a, b))[i] for i in c), '\n',
      ''.join(dict(zip(b, a))[i] for i in d))
===========================================================
'''