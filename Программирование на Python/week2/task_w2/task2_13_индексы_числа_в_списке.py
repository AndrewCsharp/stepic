"""
Напишите программу, которая считывает список чисел lst из первой строки
и число x из второй строки, которая выводит все позиции, на которых
встречается число x в переданном списке lst.

Позиции нумеруются с нуля, если число x не встречается в списке,
вывести строку "Отсутствует" (без кавычек, с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.

Sample Input 1:
5 8 2 7 8 8 2 4
8
Sample Output 1:
1 4 5

Sample Input 2:
5 8 2 7 8 8 2 4
10
Sample Output 2:
Отсутствует

"""

x = [int(i) for i in (input().split())]
y = int(input())

if y not in x:
    print("Отсутствует")
else:
    print(*[i for i in range(len(x)) if y == x[i]])

"""

l = [int(i) for i in input().split()]
x = int(input())

if x not in l:
    print("Отсутствует")
else:
    for i in range(len(l)):
        if x == l[i]:
            print(i, end=" ")

=====================================================

lst = [int(i) for i in input().split()]
num = int(input())
positions = []

for i in range(len(lst)):
    if num == lst[i]:
        positions.append(i)

if len(positions) > 0:
    print(*positions)
else:
    print("Отсутствует")
    
"""
