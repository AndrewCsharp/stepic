"""
Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.

Напишите программу, которая прочитает этот файл и подсчитает для каждого класса
средний рост учащегося.

Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост

Класс обозначается только числом. Буквенные модификаторы не используются.
Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов,
а в качестве роста используется натуральное число, но при подсчёте среднего
требуется вычислить значение в виде вещественного числа.

Выводить информацию о среднем росте следует в порядке возрастания номера
класса (для классов с первого по одиннадцатый). Если про какой-то класс
нет информации, необходимо вывести напротив него прочерк, например:

Sample Input:
6	Вяххи	159
11	Федотов	172
7	Бондарев	158
6	Чайкина	153

Sample Output:
1 -
2 -
3 -
4 -
5 -
6 156.0
7 158.0
8 -
9 -
10 -
11 172.0

dataset_3380_5.txt

"""

studentsGrowth = {"1": [0, 0, 0], "2": [0, 0, 0], "3": [0, 0, 0],
                  "4": [0, 0, 0], "5": [0, 0, 0], "6": [0, 0, 0],
                  "7": [0, 0, 0], "8": [0, 0, 0], "9": [0, 0, 0],
                  "10": [0, 0, 0], "11": [0, 0, 0]}

with open("dataset_3380_5.txt", "r") as file:
    for line in file:
        s = line.strip().split()
        studentsGrowth[s[0]][0] += int(s[2])
        studentsGrowth[s[0]][1] += 1
        studentsGrowth[s[0]][2] = studentsGrowth[s[0]][0] / studentsGrowth[s[0]][1]

for k, v in studentsGrowth.items():
    if v[2] != 0:
        print(k, v[2])
    else:
        print(k, "-")
"""

=======================================================

c = {str(i):[0]*2 for i in range(1,12)}

for l in open('in'):
    s = l.strip().split()[::2]
    c[s[0]] = [c[s[0]][0] + int(s[1]), c[s[0]][1] + 1]

[print(k + ' ', v[0]/v[1] if v[0] else '-') for k, v in c.items()]

=======================================================

d = {i:[0, 0] for i in range(1, 12)}

with open('dataset_3380_5.txt') as a:
    for i in a:
        s = i.split('\t')
        sum_height = d[int(s[0])][0] + int(s[2])
        n = d[int(s[0])][1] + 1
        d[int(s[0])] = [sum_height, n]

for i in d:
    if d[i][1] == 0:
        print(i, '-')
    else:
        print(i, d[i][0]/d[i][1])

=======================================================

classes = {i: [] for i in range(1, 12)}

with open('dataset_3380_5.txt') as f:
    for line in f:
        cls, name, height = line.strip().split('\t')
        classes[int(cls)].append(int(height))

for cls, heights in classes.items():
    print(cls, sum(heights) / len(heights) if heights else '-')

=======================================================

a = dict.fromkeys(range(1, 12), [0, 0])

for s in open('dataset_3380_5.txt', 'r').readlines():
    a[int(s.split()[0])] = [a[int(s.split()[0])][0] + int(s.split()[2]), a[int(s.split()[0])][1] + 1]

for i in a:
    print(i, '-' if a[i][1] == 0 else a[i][0] / a[i][1])

=======================================================

"""