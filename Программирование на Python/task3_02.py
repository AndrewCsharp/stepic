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
"""
