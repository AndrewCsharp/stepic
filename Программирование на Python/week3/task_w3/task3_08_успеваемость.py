"""
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя
набор строк, где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает файл с подобной структурой и для каждого
абитуриента выводит его среднюю оценку по этим трём предметам на отдельной строке,
соответствующей этому абитуриенту.

Также в конце файла, на отдельной строке, через пробел запишите средние баллы по
математике, физике и русскому языку по всем абитуриентам.

В качестве ответа на задание прикрепите полученный файл со средними оценками.

Примечание. Для разбиения строки на части по символу ';' можно использовать
метод split следующим образом:

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']

Sample Input:
    Петров;85;92;78
    Сидоров;100;88;94
    Иванов;58;72;85

Sample Output:
    85.0
    94.0
    71.666666667
    81.0 84.0 85.666666667


dataset_3363_4.txt

"""

# -*- coding: UTF-8 -*-
stud=list()
with open("dataset_3363_4.txt", "r") as file:
    for line in file:
        l = line.strip().strip()
        f, subj1, subj2, subj3 = l.split(";")
        subj1 = int(subj1)
        subj2 = int(subj2)
        subj3 = int(subj3)
        sr = (subj1 + subj2 + subj3) / 3
        stud += [[f, subj1, subj2, subj3, sr]]

srObj1=0
srObj2=0
srObj3=0
cnt = len(stud)

for l in stud:
    srObj1 += l[1] / cnt
    srObj2 += l[2] / cnt
    srObj3 += l[3] / cnt

for i in range(cnt):
    print(stud[i][4])

print(f"{srObj1} {srObj2} {srObj3}")

with open("dataset_answe.txt", "w") as file:
    for i in range(cnt):
        s = str(stud[i][4]) + "\n"
        file.write(s)
    s = f"{srObj1} {srObj2} {srObj3}\n"
    file.write(s)

"""
======================================================

s = [0, 0, 0]
n = 0
with open('111.txt') as f:
    for line in f:
        m = list(map(int, line.strip().split(';')[1:]))
        print(sum(m)/3)
        for i in 0, 1, 2: s[i] += m[i]
        n += 1
    print(s[0]/n, s[1]/n, s[2]/n)

======================================================
"""