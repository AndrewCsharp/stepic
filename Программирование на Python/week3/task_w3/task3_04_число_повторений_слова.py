"""
Когда Антон прочитал «Войну и мир», ему стало интересно, сколько
слов и в каком количестве используется в этой книге.

Помогите Антону написать упрощённую версию такой программы, которая сможет
подсчитать слова, разделённые пробелом и вывести получившуюся статистику.

Программа должна считывать одну строку со стандартного ввода и выводить для
каждого уникального слова в этой строке число его повторений (без учёта регистра)
в формате "слово количество" (см. пример вывода).

Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно
выводиться только один раз.

Sample Input 1:
a aa abC aa ac abc bcd a
Sample Output 1:
ac 1
a 2
abc 2
bcd 1
aa 2

Sample Input 2:
a A a
Sample Output 2:
a 3

"""
l = input().lower().split()
d={}

for item in l:
    cnt = l.count(item)
    d[item]=cnt
    del item

for key, value in d.items():
    print(key, value)


"""
====================================================

def cntWords(words, d):
    
    for word in words:
        i = 1
        if word in d.keys():
            d[word] = d[word] + 1
        else:
            d.update({word: 1})


s = input().lower().split()
d = dict()

cntWords(s, d)

for k, v in d.items():
    print(k, v)

====================================================

a = [i for i in input().lower().split()]
s = set(a)
for i in s:
    print(i,a.count(i))

====================================================
s = input().lower().split()
d = {}

for i in s:
    if i not in d:
        d[i] = s.count(i)

for key in d:
    print(key, d[key])
====================================================
s = input().lower().split()
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
for k, v in d.items():
    print(k,v)
====================================================
"""