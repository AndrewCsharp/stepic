"""
Напишите программу, которая считывает со стандартного ввода целые числа,
по одному числу в строке, и после первого введенного нуля выводит сумму
полученных на вход чисел.

Sample Input 1:
5
-3
8
4
0
Sample Output 1:
14

Sample Input 2:
0
Sample Output 2:
0

"""

i = 1
summa = 0

while i != 0:
    i = int(input())
    summa += i

print(summa)

"""

sum = 0
while True:
    n = int(input())
    if n != 0:
        sum += n
    else:
        break

print(sum)

"""