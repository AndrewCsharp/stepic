"""
Жители страны Малевии часто экспериментируют с планировкой комнат.
Комнаты бывают треугольные, прямоугольные и круглые.
Чтобы быстро вычислять жилплощадь, требуется написать программу,
на вход которой подаётся тип фигуры комнаты и соответствующие параметры,
которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14.

Формат ввода:
треугольник
a
b
c
где a, b и c — длины сторон треугольника

прямоугольник
a
b
где a и b — длины сторон прямоугольника

круг
r
где r — радиус окружности

Sample Input 1:
прямоугольник
4
10
Sample Output 1:
40.0

Sample Input 2:
круг
5
Sample Output 2:
78.5

Sample Input 3:
треугольник
3
4
5
Sample Output 3:
6.0

"""
typeFigure = input().lower()
sq = None

if typeFigure == "круг":
    r = int(input())
    sq = 3.14 * r ** 2
elif typeFigure == "прямоугольник":
    a, b = int(input()), int(input())
    sq = a * b
elif typeFigure == "треугольник":
    a, b, c = int(input()), int(input()), int(input())
    p = (a + b + c) / 2.0
    sq = (p * (p - a) * (p - b) * (p - c)) ** 0.5
else:
    print("Фигура не определена")

print(sq)

"""
room = input()
if room == "прямоугольник":
    print( int(input()) * int(input()) )
elif room == "круг":
    print(int(input()) ** 2 * 3.14)
elif room == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    print( (p * (p - a ) * (p - b) * (p - c)) ** 0.5 )
else:
    print('неизвестная фигура')
"""
