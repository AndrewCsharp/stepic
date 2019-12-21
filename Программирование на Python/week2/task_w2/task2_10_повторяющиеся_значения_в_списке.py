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

lst = [int(i) for i in input().split()]
lst.sort()

res = []

for i in lst :
    if i not in res and lst.count(i) > 1:
        res.append(i)



print(*res)
# or
print(" ".join(str(x) for x in res))

'''
ls = [int(i) for i in input().split()]
for i in set(ls):
    if ls.count(i) > 1:
        print(i, end=' ')
=======================================
a=input().split()
[a.remove(i) for i in set(a)]
print(*set(a))
=======================================
s = input().split()
print (*(i for i in set(s) if s.count(i) > 1))
'''
