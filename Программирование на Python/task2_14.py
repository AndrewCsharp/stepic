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

"""

nums = []
row = 0

while True:
    s = input()

    if s == 'end':
        break

    s = s.split()
    nums += s
    row += 1

col = len(nums) // row
sourceMatrix = [[0 for j in range(col)] for i in range(row)]
resMatrix = [[0 for j in range(col)] for i in range(row)]
cntSimbol = 0

for i in range(0, row):
    for j in range(0, col):
        sourceMatrix[i][j] = int(nums[cntSimbol])
        cntSimbol += 1

for i in range(0, row):
    for j in range(0, col):
        num1 = sourceMatrix[i-1][j]
        num2 = sourceMatrix[i][j-1]
        num3 = sourceMatrix[i - row + 1][j]
        num4 = sourceMatrix[i][j - col + 1]
        resMatrix[i][j] = num1 + num2 + num3 + num4

for i in range(0, row):
    print(*resMatrix[i])


"""
=================================================================
nums = []
row  = 0

while True:
    s = input()

    if s == 'end':
        break

    s = s.split()
    nums += s
    row += 1

col = len(nums) // row
sourceMatrix = [[0 for j in range(col)] for i in range(row)]
resMatrix = [[0 for j in range(col)] for i in range(row)]
cntSimbol = 0

for i in range(0, row):
    for j in range(0, col):
        sourceMatrix[i][j] = int(nums[cntSimbol])
        cntSimbol += 1

for i in range(0, row):
    for j in range(0, col):
        num1 = sourceMatrix[i-1][j]
        num2 = sourceMatrix[i][j-1]
        num3 = sourceMatrix[i - row + 1][j]
        num4 = sourceMatrix[i][j - col +1]
        resMatrix[i][j] = num1 + num2 + num3 + num4

for i in range(0, row):
    print(*resMatrix[i])
=================================================================
nums = []
row  = 0

while True:
    s = input()

    if s == 'end':
        break

    s = s.split()
    nums += s
    row += 1

col = len(nums) // row
m = [[0 for j in range(col)] for i in range(row)]
cM = [[0 for j in range(col)] for i in range(row)]
ii = 0

for i in range(0, row):
    for j in range(0, col):
        m[i][j] = int(nums[ii])
        ii += 1

for i in range(0, row):
    for j in range(0, col):
        num1 = m[i-1][j]
        num2 = m[i][j-1]
        num3 = m[i - row + 1][j]
        num4 = m[i][j - col +1 ]
        cM[i][j] = num1 + num2 + num3 + num4

for i in range(0, row):
    print(*cM[i])
=================================================================
nums = []
row  = 0

while True:
    s = input()

    if s == 'end':
        break

    s = s.split()
    nums += s
    row+=1

col = len(nums)// row
m = [[0 for j in range(col)]  for i in range(row)]
finM = [[0 for j in range(col)]  for i in range(row)]
ii = 0

for i in range(0, row):
    for j in range(0, col):
        m[i][j] = int(nums[ii])
        ii+=1

if row == 1 and col > 1:
    for j in range(0, col):
        if j == 0:
            finM[0][j] = m[0][j] * 2 + m[0][1] + m[0][-1]
        elif j == col-1:
            finM[0][j] = m[0][j] * 2 + m[0][0] + m[0][j-1]
        else:
            finM[0][j] = m[0][j] * 2 + m[0][j-1] + m[0][j+1]
elif col == 1 and row > 1:
    for i in range(0, row):
        if i == 0:
            finM[0][0] = m[0][0] * 2 + m[1][0] + m[-1][0]
        elif i == row-1:
            finM[i][0] = m[i][0] * 2 + m[0][0] + m[i-1][0]
        else:
            finM[i][0] = m[i][0] * 2 + m[i+1][0] + m[i-1][0]
elif row > 1 and col > 1:#(i-1, j), (i+1, j), (i, j-1), (i, j+1)
    for i in range(0, row):
        for j in range(0, col):
            if i == 0 and j == 0:
                num1 = m[0][1]
                num2 = m[0][-1]
                num3 = m[1][0]
                num4 = m[-1][0]
                finM[i][j] = num1 + num2 + num3 + num4
            elif i == 0 and j == col - 1:
                num1 = m[0][0]
                num2 = m[0][j-1]
                num3 = m[i+1][j]
                num4 = m[-1][j]
                finM[i][j] = num1 + num2 + num3 + num4
            elif i == row - 1 and j == col - 1:
                num1 = m[i][0]
                num2 = m[i][j-1]
                num3 = m[i-1][j]
                num4 = m[0][j]
                finM[i][j] = num1 + num2 + num3 + num4
            elif i == row-1 and j == 0:
                num1 = m[i][1]
                num2 = m[i][-1]
                num3 = m[0][0]
                num4 = m[i-1][0]
                finM[i][j] = num1 + num2 + num3 + num4
            elif i == 0 and 0 < j < col - 1:
                num1 = m[0][j-1]
                num2 = m[0][j+1]
                num3 = m[i+1][j]
                num4 = m[-1][j]
                finM[i][j] = num1 + num2 + num3 + num4
            elif i == row - 1 and 0 < j < col - 1:
                num1 = m[i][j-1]
                num2 = m[i][j+1]
                num3 = m[0][j]
                num4 = m[i-1][j]
                finM[i][j] = num1 + num2 + num3 + num4
            elif 0 < i < row - 1 and j == 0:
                num1 = m[i][j+1]
                num2 = m[i][-1]
                num3 = m[i+1][0]
                num4 = m[i-1][0]
                finM[i][j] = num1 + num2 + num3 + num4
            elif 0 < i < row - 1 and j == col - 1:
                num1 = m[i][0]
                num2 = m[i][j-1]
                num3 = m[i+1][j]
                num4 = m[i-1][j]
                finM[i][j] = num1 + num2 + num3 + num4
            else:
                num1 = m[i][j-1]
                num2 = m[i][j+1]
                num3 = m[i+1][j]
                num4 = m[i-1][j]
                finM[i][j] = num1 + num2 + num3 + num4
else:
    finM[i][j] = m[i][j] * 4


for i in range(0, row):
    print(*finM[i])
=================================================================
"""
