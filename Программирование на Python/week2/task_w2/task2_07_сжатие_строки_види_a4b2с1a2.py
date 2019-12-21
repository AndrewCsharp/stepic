"""
Узнав, что ДНК не является случайной строкой, только что поступившие
в Институт биоинформатики студенты группы информатиков предложили
использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых
символов исходной строки заменяются на этот символ и количество его
повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным
алгоритмом и выводит закодированную последовательность на стандартный вывод.
Кодирование должно учитывать регистр символов.

Sample Input 1:
aaaabbcaa
Sample Output 1:
a4b2c1a2

Sample Input 2:
abc
Sample Output 2:
a1b1c1

"""

s = input() + " "
code = ""
cnt = 1

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        cnt += 1
    else:
        code += s[i] + str(cnt)
        cnt = 1

print(code)

"""
strA = input()
strB = ""

i = 0

while i < (len(strA)):
    cnt = 1
    ch = strA[i]
    j = 1 + i

    while j < len(strA):
        nextCh = str(strA[j])
        if ch == nextCh:
            cnt += 1
            j += 1
        else:
            break

    strB += (ch + str(cnt))
    i += cnt

print(strB)

=======================================================

sIn = input()
sOut = ""

i = 0
while i < len(sIn):
    j = i+1

    if i != len(sIn)-1:
        while j < len(sIn) and sIn[i] == sIn[j]:
            j += 1

        cnt = sIn[i:j].count(sIn[i])
        sOut += sIn[i] + str(cnt)
        i += cnt
    else:
        sOut += sIn[i] + "1"
        break

print(sOut)

=======================================================

a = input() + '0'
c = a[0]
x = ''
for i in a[1:]:
    if i == c[0]:
        c = c + i
    else:
        x = x + c[0] + str(len(c))
        c = i
print(x)

=======================================================

str = input()
i = 0
sum = 1
while i < len(str)-1:
    if str[i] == str [i + 1]:
        sum += 1
    else:
        print (str[i], sum, sep = "", end = "")
        sum = 1
    i += 1

print (str[i], sum, sep = "", end = "")

=======================================================

s = input()
k = 1

for i in range(1,len(s)):
    if s[i]==s[i-1]:
        k+=1
    else:
        print(s[i-1 ], end='')
        print(k, end='')
        k = 1

print(s[-1],end='')
print(k)
=======================================================

"""
