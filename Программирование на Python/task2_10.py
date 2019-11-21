"""
Напишите программу, которая принимает на вход список чисел в одной строке
и выводит на экран в одну строку значения, которые повторяются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.

Sample Input 1:
4 8 0 3 4 2 0 3
Sample Output 1:
0 3 4

Sample Input 2:
10
Sample Output 2:


Sample Input 3:
1 1 2 2 3 3
Sample Output 3:
1 2 3

Sample Input 4:
1 1 1 1 1 2 2 2
Sample Output 4:
1 2

"""
a = [i for i in input().split()]
a.sort()
b = []

for i in a:
  if (a.count(i) > 1) and (i not in b):
    b.append(i)

s = " ".join(str(x) for x in b)
print(s)

"""
a = [int(i) for i in input().split()]
b = ''
s = set(a)
for item in s:
    if  a.count(item) > 1:
        b +=str(item) + " "

print(b)
===================================================
a = [int(i) for i in input().split()]
a.sort()
b = []
s=''
for item in a:
    if item not in b:
        cnt = a.count(item)
        if cnt  > 1:
            b.append(item)

s = " ".join(str(x) for x in b)
print(s)

"""