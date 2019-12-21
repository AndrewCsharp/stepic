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

a = int(input())
b = int(input())
c = int(input())

if a >= b >= c:
    print(a, c, b, sep="\n" )
elif a >= c >= b:
    print(a, b, c, sep="\n")
elif b >= a >= c:
    print(b, c, a, sep="\n")
elif b >= c >= a:
    print(b, a, c, sep="\n")
elif c >= a >= b:
    print(c, b, a, sep="\n")
elif c >= b >= a:
    print(c, a, b, sep="\n")

"""
a = int(input())
b = int(input())
c = int(input())

maxi = a
if maxi < b:
    maxi = b
if maxi < c:
    maxi = c

mini = a
if mini >  b:
    mini = b
if mini > c:
    mini = c

avr = (a + b + c) - maxi - mini

print(maxi, mini, avr, sep="\n")

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

a = int(input())
b = int(input())
c = int(input())

maxNum = max(a, b, c)
minNum = min(a, b, c)
remainingNum = (a + b + c) - (maxNum+minNum)
print(maxNum, minNum, remainingNum, sep="\n")

=================================================

a, b, c = int(input()), int(input()), int(input())

list = [a, b, c]
list.sort()

print(list[2])
print(list[0])
print(list[1])

=================================================

"""

