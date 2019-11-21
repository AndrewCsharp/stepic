"""
Напишите программу, которая выводит часть последовательности
 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
 (число повторяется столько раз, чему равно).
На вход программе передаётся неотрицательное целое число n — столько
элементов последовательности должна отобразить программа.
На выходе ожидается последовательность чисел, записанных через
пробел в одну строку.

Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

Sample Input:
7
Sample Output:
1 2 2 3 3 3 4

"""
cntAll = int(input())
cntPrint = 0
answer = []

for i in range(1, cntAll + 1):
    j = 0
    while j < i and cntPrint < cntAll:
        answer += [i]
        cntPrint += 1
        j += 1

print(*answer)

"""
cntAll = int(input())
cntPrint = 0
answer = ''

for i in range(1, cntAll + 1):
    j = 0
    while j < i and cntPrint < cntAll:
        answer += str(i) + " "
        cntPrint += 1
        j += 1

print(answer)
=======================================================
cntAll = int(input())
cntPrint = 0
answer = ''

for i in range(1, cntAll + 1):
    j = 1
    while j <= i:
        if cntPrint < cntAll:
            answer += str(i) + " "
            j += 1
            cntPrint += 1
        else:
            break

answer = answer[:-1]
print(answer)
=======================================================
cntAll = int(input())
cntPrint = 0
answer = ''

for i in range(1, cntAll + 1):
    j = 1
    while j <= i:
        if  cntPrint < cntAll:
            answer += str(i) + " "
            j += 1
            cntPrint += 1
        else:
            break

answer= answer[:-1]
print(answer)
=======================================================
num = int(input())
i = 1
s = []
cnt = 0
a = ""
if num > 0:
    while i <= num:
        s+= [i] * i
        i+=1

    for i in range(len(s)):
        if i < num:
            a += str(s[i]) + " "

    print(a)

else:
    print('0')
=======================================================

"""