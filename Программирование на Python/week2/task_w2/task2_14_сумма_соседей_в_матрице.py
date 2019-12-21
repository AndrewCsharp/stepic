"""
Напишите программу, на вход которой подаётся прямоугольная матрица
в виде последовательности строк, заканчивающихся строкой,
содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый
элемент в позиции i, j равен сумме элементов первой матрицы на
позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
У крайних символов соседний элемент находится с противоположной
стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по
соответствующему направлению.

Sample Input 1:
9 5 3
0 7 -1
-5 2 9
end
Sample Output 1:
3 21 22
10 6 19
20 16 -1

Sample Input 2:
1
end
Sample Output 2:
4



Маленькая подсказка для меня (n - кол-во эл в массиве)
right = i - n + 1
left = i % n - 1

rows = len(input)    # 3 rows in your example
cols = len(input[0]) # 2 columns in your example

"""

matrix = list()
res = list()

while True:
    s = input()
    if "end" != s:
        matrix.append([int(i) for i in s.split()])
        #matrix += [list(map(int, s.split()))]
    else:
        break

#       v2
#       s, matrix = input(), []
#       while s != 'end':
#           matrix.append([int(i) for i in s.split()])
#           s = input()

if not matrix:
    print("Empty")
    exit()

rows = len(matrix)
cols = len(matrix[0])
res = [[0 for j in range(cols)] for i in range(rows)]

for i in range(rows):
    for j in range(cols):
        n1 = matrix[i-1][j]
        n3 = matrix[i][j - 1]
        n2 = matrix[i + 1 - rows][j]
        n4 = matrix[i][j + 1 - cols]
        res[i][j] = n1 + n2 + n3 + n4
        ################################
        #   v2
        #   leftNum = matrix[i % rows - 1][j]
        #   rightNum = matrix[i - rows + 1][j]
        #   upNum = matrix[i][j % cols - 1]
        #   downNum = matrix[i][j - cols + 1]
        #   res[i][j] = leftNum + rightNum + upNum + downNum

for row in res:
    print(*row)

#   v2
#   for i in range(rows):
#       print(*res[i])

"""
1)В массив {a}  получаем данные
2)В массив {b} вносим данные из {a} преобразовывая
тип данных в int
3)Узнаем размеры массива {h,w} (высота и ширина) и
создаем массив {c} заполненный нулями
4)Заполняем {c}. При заполнении используем отрицательные
индексы, если есть риск вылезти за границы ({h,w})
i = i - h; j = j - w
5)Вывести

a = []
while True:
    a.append(input().split())
    if a[len(a)-1][0] == 'end':
        break
b = []
for i in range(len(a)-1):
    b.append([int(j) for j in a[i]])

h = len(b)
w = len(b[0])
c = [[0 for j in range(w)] for i in range(h)]

for i in range(h):
    for j in range(w):
        c[i][j] = b[i-h+1][j] + b[i-1][j] + b[i][j-w+1] + b[i][j-1]

for i in range(h):
    for j in range(w):
        print(c[i][j], end=' ')
    print()

"""
