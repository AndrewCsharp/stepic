"""
Напишите программу, на вход которой подаётся список чисел одной строкой.
Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
Для элементов списка, являющихся крайними, одним из соседей считается элемент,
находящий на противоположном конце этого списка. Например, если на вход подаётся
список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.

Sample Input 1:
1 3 5 6 10
Sample Output 1:
13 6 9 15 7

Sample Input 2:
10
Sample Output 2:
10

"""
a = [int(i) for i in input().split()]
lenList = len(a)

if lenList == 1:
    print(a[0])
else:
    for i in range(lenList):
        if i == 0:
            print(a[1] + a[lenList - 1], end=" ")
        elif i == lenList - 1:
            print(a[0] + a[lenList - 2])
        elif i > 0 and i < lenList - 1:
            print(a[i - 1] + a[i + 1], end=" ")

"""
s=[int (i) for i in input().split()]

if len(s)==1:
    print (s[0])
else:
    for i in range(len(s)):
        print(s[i-1]+s[(i+1)%len(s)],end=' ')

=============================================================================

l = [int(i) for i in input().split()]
lRes = list()

if len(l) == 1:
    lRes.append(l[0])
else:
    for i in range(len(l)):
        if i == 0:
            lRes.append(l[1] + l[len(l)-1])
            #print(l[1] + l[(len(l)-1)])

        elif i == len(l)-1:
            lRes.append(l[len(l)-2] + l[0])
            #print(l[(len(l)-2)] + l[0])

        else:
            lRes.append(l[i-1] + l[i+1])
            #print(l[(i-1)] + l[(i+1)])


print(*lRes)

"""
