"""
Напишите программу, на вход которой даются четыре числа a, b, c и d,
каждое в своей строке. Программа должна вывести фрагмент таблицы
умножения для всех чисел отрезка [a;b] на все числа отрезка [c;d].

Числа a, b, c и d являются натуральными и не превосходят 10, a≤b, c≤d.

Следуйте формату вывода из примера, для разделения элементов
внутри строки используйте '\t' — символ табуляции. Заметьте, что
левым столбцом и верхней строкой выводятся сами числа из заданных
отрезков — заголовочные столбец и строка таблицы.


Sample Input 1:
7
10
5
6
Sample Output 1:
	5	6
7	35	42
8	40	48
9	45	54
10	50	60


Sample Input 2:
5
5
6
6
Sample Output 2:
	6
5	30

Sample Input 3:
1
3
2
4
Sample Output 3:
	2	3	4
1	2	3	4
2	4	6	8
3	6	9	12

"""
a, b, c, d = [int(input()) for i in range(4)]

for i in range(a - 1, b + 1):
    for j in range(c - 1, d + 1):
        if i == a - 1 and j == c - 1:
            print("\t", end="")
        if i == a - 1 and j > c - 1:
            print(j, "\t", end="")
        if i > a - 1 and j == c - 1:
            print(i, "\t", end="")
        if i > a - 1 and j > c - 1:
            print(i * j, "\t", end="")
    print()

"""
a, b, c, d = [int(input()) for i in range(4)]

rows = [i for i in range(a, b+1)]
cols = [j for j in range(c, d+1)]

print(" ", *cols, sep="\t")

for i in rows:
    print(i, "\t", end="")
    for j in cols:
        print(i * j, "\t", end="")
    print()

"""