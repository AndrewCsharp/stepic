"""
Напишите программу, которая получает на вход три целых числа,
по одному числу в строке, и выводит на консоль в три строки
сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.

Sample Input 1:
8
2
14
Sample Output 1:
14
2
8

Sample Input 2:
23
23
21
Sample Output 2:
23
21
23

"""

a, b, c = [int(input()) for i in range(3)]

if a >= b >= c:
    print(a, '\n', c,'\n', b)
elif a >= c >= b:
    print(a, '\n', b,'\n', c)
elif b >= a >= c:
    print(b, '\n', c,'\n', a)
elif b >= c >= a:
    print(b, '\n', a,'\n', c)
elif c >= a >= b:
    print(c, '\n', b,'\n', a)
elif c >= b >= a:
    print(c, '\n', a,'\n', b)


"""
=================================================
a, b, c = [int(input()) for i in range(3)]

m = a
l = a

if m < b:
    m = b
if m < c:
    m = c
if l > b:
    l = b
if l > c:
    l = c

print(m)
print(l)
print((a+b+c)-(m+l))

=================================================

a,b,c = int(input()), int(input()), int(input())

if a - b < 0:
    a, b = b, a
if a - c < 0:
    a, c = c, a
if b - c < 0:
    b, c = c, b

print(a)
print(c)
print(b)

=================================================

a,b,c = int(input()), int(input()), int(input())

if b < a:
    a,b = b,a
if c < b:
    b,c = c,b
if b < a:
    a,b = b,a
print(c,a,b, sep = '\n')

=================================================

a, b, c = int(input()), int(input()), int(input())
s = a + b + c

print(max(a,b,c))
print(min(a,b,c))
print(s - max(a,b,c) - min(a,b,c))

=================================================
a, b, c = int(input()), int(input()), int(input())

list = [a, b, c]
list.sort()

print(list[2])
print(list[0])
print(list[1])

"""
