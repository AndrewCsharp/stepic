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
strSource = input()
strEncode = strSource + " "
res = ""
cnt = 1

for i in range(len(strEncode)-1):
    if strEncode[i] == strEncode[i+1]:
        cnt += 1
    else:
        res += strEncode[i] + str(cnt)
        cnt = 1

print(res)

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
"""