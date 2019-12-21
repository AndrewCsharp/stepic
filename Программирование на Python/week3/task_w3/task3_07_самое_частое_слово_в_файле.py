"""
Недавно мы считали для каждого слова количество его вхождений в строку.
Но на все слова может быть не так интересно смотреть, как, например,
на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может
быть больше одной строки) и выводит самое частое слово в этом тексте
и через пробел то, сколько раз оно встретилось. Если таких слов несколько,
вывести лексикографически первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC

Sample Output:
abc 3

dataset_3363_3.txt

"""
l_words=[]
d_words = {}
maxNum = 0
frequent_word = []

with open("dataset_3363_3.txt") as file:
    for line in file:
        l_words += line.lower().strip().split()

for s in l_words:
    if s not in d_words:
        d_words[s] = l_words.count(s)
    else:
        continue

maxNum = max(d_words.values())

for k, v in d_words.items():
    if v == maxNum:
        frequent_word.append(k)

frequent_word.sort()

with open("dataset_3363_3_answ.txt", "w") as file:
    file.write(str(*frequent_word) + " " + str(maxNum))

print("done !")

"""
===============================================================

with open('dataset_3363_3.txt') as inf, open('MostPopularWord.txt','w') as ouf:
    maxc = 0
    s = inf.read().lower().strip().split()
    s.sort()
    for word in s:
        counter = s.count(word)
        if counter > maxc:
            maxc = counter
            result_word = word
    ouf.write(result_word +' ' + str(maxc))

===============================================================

all = open('dataset.txt', 'r')
s = all.read().lower().strip().split()
y = 0
m =''
for i in s:
    z = s.count(i)
    if z >= y:
        y = z
        m = i
print(m, y)

===============================================================

with open('gtx.txt','r') as file:
    s = file.read().strip().lower().split()

z = {i: s.count(i) for i in s}

maximum = max(z, key=z.get)
x = {maximum: z[maximum]}

with open('gtx.txt','w') as file:
    file.write(str(x))

===============================================================

words = []

with open('dataset_3363_3.txt') as inf:
    for line in inf:
        words += line.strip().lower().split()
n = 0
w = []

for word in set(words):
    count = words.count(word)
    if count >= n:
        if count > n:
            w = []
        n = count
        w.append(word)

print(min(w), n)

===============================================================

with open('dataset_xxx.txt') as file:
    dct = {}
    for line in file:
        lst = [i.lower() for i in line.strip().split()]
        for i in lst:
            dct.update({i: int(dct.get(i, 0)) + 1})

    m = max(dct, key=(lambda key: dct[key]))
    print(m, dct[m])

===============================================================

with open('dataset.txt', 'r') as x:
    x = "".join(s.readlines()).split()

m = max([x.count(f) for f in x])
t = [g for g in x if x.count(g) == m][0]
print(t, m)

===============================================================

with open('1.txt') as string:
    s1 = string.read().replace('\n', ' ').lower().split()

a = max(s1, key=s1.count)
print(a, s1.count(a))

===============================================================

d = open('input.txt').read().lower().split()
s = {}
for x in d:
    s.setdefault(d.count(x), x)

print(s.get(max(s.keys()))," ", max(s.keys()))

===============================================================

from collections import Counter

c = Counter(sorted(s.lower().split())).most_common()
print(c[0][0], c[0][1])

===============================================================

from collections import Counter
with open('input.txt') as inpt:
    words = inpt.read().lower().split()

d = dict(Counter(words))
srted = dict(sorted(d.items()))
res_key = max(srted, key=srted.get)
print(res_key, srted.get(res_key))

===============================================================
"""