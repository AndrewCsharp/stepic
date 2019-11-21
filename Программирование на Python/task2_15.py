"""
Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке,
как показано в примере (здесь n=5):

Sample Input:
5

Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

"""
N = int(input())

m = [[0 for j in range(N)] for i in range(N)]

step = 0
num = 1
n = N

while step < n:

    for j in range(step, n):
        i = step
        m[i][j] = num
        num += 1

    for i in range(step + 1, n):
        j = n - 1
        m[i][j] = num
        num += 1

    for j in range(n - 2, step - 1, -1):
        i = n - 1
        m[i][j] = num
        num += 1

    for i in range(n - 2, step, -1):
        j = step
        m[i][j] = num
        num += 1

    step += 1
    n -= 1

for i in range(0, N):
    print(*m[i])

"""
N = int(input())

m = [[0 for j in range(N)] for i in range(N)]

step = 0
num = 1
n = N

while step <= n:
    j = step
    i = step
    while j < n:
        m[i][j] = num
        num += 1
        j += 1

    num -= 1
    j = n - 1
    while i < n:
        m[i][j] = num
        num += 1
        i += 1

    num -= 1
    i = n - 1
    while j >= step:
        m[i][j] = num
        num+=1
        j-=1

    num -= 1
    j += 1
    while i > step:
        m[i][j] = num
        num+=1
        i -= 1

    step += 1
    n -= 1

print()
for i in range(0, N):
    print(*m[i])
"""