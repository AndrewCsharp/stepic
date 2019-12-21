"""
Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
удаляет из него все нечётные значения, а чётные нацело делит на два.
Функция не должна ничего возвращать, требуется только изменение переданного списка,
например:
        lst = [1, 2, 3, 4, 5, 6]
        print(modify_list(lst))  # None
        print(lst)               # [1, 2, 3]
        modify_list(lst)
        print(lst)               # [1]

        lst = [10, 5, 8, 3]
        modify_list(lst)
        print(lst)               # [5, 4]

Функция не должна осуществлять ввод/вывод информации.

"""

def modify_list(l):
    i=0
    while i<len(l):
        if l[i]%2 != 0:
            del l[i]
        else:
            l[i]=l[i]//2
            i+=1

"""

def modify_list(l):
    cnt = len(l)-1
    while cnt >= 0:
        if l[cnt] % 2 != 0:
            del l[cnt]
        cnt-=1

    if len(l) > 0:
        for i in range(len(l)):
            l[i] = l[i] // 2

==================================================

def modify_list(l):
    i = 0

    while i < len(l):
        if l[i] % 2 != 0:
            del l[i]
            i = 0
        else:
            i += 1
    i = 0
    while i < len(l):
        l[i] = l[i] // 2
        i += 1

==================================================

def modify_list(l):
    i = 0
    for x in range(len(l)):
        if l[i] % 2 == 1:
            l.remove(l[i])
        else:
            l[i] = l[i] // 2
            i += 1

==================================================
# def modify_list(l):
#     x = []
#     for i in range(len(l)):
#         if l[i]%2 == 0:
#             x.append(int(l[i])//2)
#
#     l.clear()
#     for i in range(len(x)):
#         l.append(x[i])
==================================================
# def modify_list(s):
#     k=[]
#     for i in range(0, len(s)):
#         if s[i] % 2 == 0:
#             k.append(int(s[i]/2))
#     s.clear()
#     s += k
"""
