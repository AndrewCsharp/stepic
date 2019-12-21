"""
Напишите функцию update_dictionary(d, key, value), которая принимает
на вход словарь d и два числа: key и value.

Если ключ key есть в словаре d, то добавьте значение value в список,
который хранится по этому ключу. Если ключа key нет в словаре,
то нужно добавить значение в список по ключу 2∗key.
Если и ключа 2∗key нет, то нужно добавить ключ 2∗key в словарь
и сопоставить ему список из переданного элемента [value].

Требуется реализовать только эту функцию, кода вне неё не должно быть.
Функция не должна вызывать внутри себя функции input и print.

Пример работы функции:

        d = {}
        print(update_dictionary(d, 1, -1))  # None
        print(d)                            # {2: [-1]}
        update_dictionary(d, 2, -2)
        print(d)                            # {2: [-1, -2]}
        update_dictionary(d, 1, -3)
        print(d)                            # {2: [-1, -2, -3]}

"""

def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif 2*key in d:
        d[2*key].append(value)
    else:
        d[2*key] = [value]

"""
============================================================
def update_dictionary(d, key, value):
    if key in d:
        l = list(d[key])
        l+=[value]
        d[key] = l
    else:
        k = 2*key
        if k in d:
            l = list(d[k])
            l+=[value]
            d[k] = l
        else:
            l = [value]
            d[k] = l
============================================================
def update_dictionary(d, key, value):
    if key in d.keys():
        d[key].append(value)
    else:
        if 2*key in d.keys():
            d[2*key].append(value)
        else:
            d.update({2*key:[value]})


d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}
============================================================
def update_dictionary(d, key, value):
    if key in d:
        d.get(key).append(value)
    else:
        if 2*key in d:
            d.get(2*key).append(value)
            return
        d.update({2*key:[value]})
============================================================
def update_dictionary(d: dict, key: int, value: int):
    if key in d:
        d[key] += [value]
    else:
        if 2 * key in d:
            d[2 * key] += [value]
        else:
            d[2 * key] = [value]
============================================================

"""