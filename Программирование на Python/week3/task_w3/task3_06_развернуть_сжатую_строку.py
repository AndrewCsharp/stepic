"""
На прошлой неделе мы сжимали строки, используя кодирование повторов.
Теперь нашей задачей будет восстановление исходной строки обратно.

Напишите программу, которая считывает из файла строку, соответствующую тексту,
сжатому с помощью кодирования повторов, и производит обратную операцию,
получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после
нажатия "Start Quiz" у вас появляется ссылка "download your dataset".
Используйте эту ссылку для того, чтобы загрузить файл со входными данными
к себе на компьютер. Запустите вашу программу, используя этот файл в качестве
входных данных. Выходной файл, который при этом у вас получится, надо отправить
в качестве ответа на эту задачу.

Sample Input:
a3b4c2e10b1
Sample Output:
aaabbbbcceeeeeeeeeeb


dataset_3363_2.txt

"""
with open('dataset_3363_2.txt') as fl:
    s = fl.readline().strip()

l = list()
ch = ""
cnt = 0
i = 0
while i < len(s):
    if s[i].isalpha():
        ch = s[i]
    else:
        if s[i] == "_":
            break
        elif s[i].isdigit() and s[i + 1].isdigit():
            cnt = (int(s[i])) * 10 + int(s[i + 1])
            i += 1
        else:
            cnt = int(s[i])

        l += [[ch, cnt]]
    i += 1

res = ""
for i in l:
    for j in range(i[1]):
        res += i[0]

with open('dataset_3363_2_answ.txt', 'w') as ofl:
    ofl.write(res)

print(res)
print('done')

"""
===========================================================================
with open("dataset_3363_2.txt") as file:
    s= file.readline().strip()

subs =[]
nums=[]

i=0
while i < len(s):
    if not s[i].isdigit():
        subs += [s[i]]
    i+=1

for item in subs:
    s = s.replace(item, " ")

s = s.strip()
nums = s.split(' ')

i=0
answ=''
while i < len(subs):
    n = int(nums[i])
    j=0
    while j<n:
        answ+=subs[i]
        j+=1
    i+=1

with open("answer.txt", "w") as file:
    file.write(answ)

print('done')

===========================================================================

s = input()
d = []
for i in s:
    if not i.isdigit(): d.append(i)
    else: d[-1] += i
print(*[i[0]*int(i[1:]) for i in d], sep='')

===========================================================================

with open('dataset_3363_2.txt', 'r') as f:
    s = f.readline().strip()

i = 0
while i < len(s):
    j = i + 1

    while j < len(s) and s[j].isdigit():
        j += 1

    print(s[i] * int(s[i+1:j]), end='')
    i = j

===========================================================================

with open('inp.txt') as inf:
    s = inf.readline()

n = ''

for i in s:
    if i.isdigit():
        n += str(i)
    else:
        n += ' ' + i + ' '

l = n.split()
rs = ''

for i in range(0, len(l), 2):
    rs += l[i] * int(l[i + 1])

with open('out.txt', 'w') as ouf:
    ouf.write(rs)

===========================================================================
"""