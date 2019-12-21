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

num = int(input())
cnt = 1
res = []
for i in range(1, num+1):
        j = 1
        while j <= i and cnt <= num:
            res.append(i)
            j += 1
            cnt += 1

print(*res)

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

==========================================

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

==========================================

n = int(input())
i = 1
cnt = n

while i <= n:
    j = i
    while j > 0:
        if cnt > 0:
            print(i, end=" ")
            cnt -= 1
        else:
            break
        j -= 1
    i += 1

"""

# ==== гыдота ещё та =========================
# n = int(input())
# i = 0
# s = ""
# while i < n:
#     s += str(i) * i
#     i += 1
#
# print(s[0:n])
