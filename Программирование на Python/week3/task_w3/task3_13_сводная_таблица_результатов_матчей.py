"""
Напишите программу, которая принимает на стандартный вход список
игр футбольных команд с результатом матча и выводит на стандартный
вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.


Sample Input:
3
Зенит;3;Спартак;1
Спартак;1;ЦСКА;1
ЦСКА;0;Зенит;2

Sample Output:
Зенит:2 2 0 0 6
ЦСКА:2 0 1 1 1
Спартак:2 0 1 1 1

"""
cntGames = int(input())
games=[]
comands=dict()

for i in range(cntGames):
    res = input().split(";")
    games += [res]

for i in range(len(games)):
    for j in range(0, len(games[0]), 2):
        comands[games[i][j]] = [0]*4

for key in comands:
    all, win, nichiya, ups, bali = 0, 0, 0, 0, 0

    for i in range(len(games)):
        if key == games[i][0]:
            if int(games[i][1]) > int(games[i][3]):
                all+=1
                win+=1
            if int(games[i][1]) == int(games[i][3]):
                all+=1
                nichiya+=1
            if int(games[i][1]) < int(games[i][3]):
                all+=1
                ups+=1

        if key == games[i][2]:
            if int(games[i][3]) > int(games[i][1]):
                all+=1
                win+=1
            if int(games[i][3]) == int(games[i][1]):
                all+=1
                nichiya+=1
            if int(games[i][3]) < int(games[i][1]):
                all+=1
                ups+=1

    bali= win*3 + nichiya
    comands[key] = [all, win, nichiya, ups, bali]

for key in comands:
	print(f"{key}: {comands[key][0]} {comands[key][1]} {comands[key][2]} {comands[key][3]} {comands[key][4]}")

"""
============================================================
cntGames = int(input())
games = list()
teams = dict()

i = 0
while i < cntGames:
    s = input().split(";")
    games += [[s[0], int(s[1]), s[2], int(s[3])]]
    if s[0] not in teams:
        teams.update({s[0]: list()})
    if s[2] not in teams:
        teams.update({s[2]: list()})
    i += 1

for key in teams.keys():
    i = 0
    cnt = 0
    win = 0
    deadheat = 0
    defeat = 0
    ball = 0

    while i < cntGames:
        if key == games[i][0]:
            if games[i][1] > games[i][3]:
                win += 1
            elif games[i][1] == games[i][3]:
                deadheat += 1
            else:
                defeat += 1
            cnt += 1
        if key == games[i][2]:
            if games[i][3] > games[i][1]:
                win += 1
            elif games[i][3] == games[i][1]:
                deadheat += 1
            else:
                defeat += 1
            cnt += 1
        i += 1

    ball = win * 3 + deadheat
    teams[key] = [cnt, win, deadheat, defeat, ball]

for team in teams.keys():
    statistic = str(teams[team]).strip('[]').replace(',', '')
    print(f"{team}:{statistic}")
============================================================
def command(c, res):
    if not c in dct: dct[c] = [0, 0, 0, 0, 0]
    dct[c] = [dct[c][0] + 1, 
                dct[c][1] + 1 if res == 3 else dct[c][1],
                dct[c][2] + 1 if res == 1 else dct[c][2],
                dct[c][3] + 1 if res == 0 else dct[c][3],
                dct[c][4] + res,]  
dct = {}
for i in range(int(input())):
    c1, g1, c2, g2 = input().split(';')    
    command(c1, 3 if g1 > g2 else 1 if g1 == g2 else 0)
    command(c2, 3 if g2 > g1 else 1 if g1 == g2 else 0)
for c in dct:
    print('{}:{} {} {} {} {}'.format(c, *dct[c]))
============================================================
В стандартной библиотеке есть база данных, так что пуркуа бы и не па.

import sqlite3

with sqlite3.connect(":memory:") as db:
    db.execute('CREATE TABLE stat(team TEXT, win INT, draw INT, lose INT)')
    
    def record(t, s1, s2):
        db.execute('INSERT INTO stat VALUES (?, ?, ?, ?)', (t, s1>s2, s1==s2, s1<s2))

    n = int(input())
    for _ in range(n):
        t1, s1, t2, s2 = input().split(';')
        record(t1, int(s1), int(s2))
        record(t2, int(s2), int(s1))
    db.commit()
    
    statq = 'SELECT team, SUM(win), SUM(draw), SUM(lose) FROM stat GROUP BY 1'
    for t, w, d, l in db.execute(statq):
        print(f'{t}:{w+d+l} {w} {d} {l} {3*w + d}')  

============================================================

games, table = [input().split(';') for i in range(int(input()))], {}
for t1, s1, t2, s2 in games:
    table[t1] = [i+j for i, j in zip(table.setdefault(t1, [0,0,0,0]), [1, (s1>s2), (s1==s2), (s1<s2)])]
    table[t2] = [i+j for i, j in zip(table.setdefault(t2, [0,0,0,0]), [1, (s2>s1), (s2==s1), (s2<s1)])]
print(*(i+':'+' '.join(map(str, j))+' '+str(j[1]*3+j[2]) for i, j in table.items()), sep='\n')

============================================================
r = {}
def add_r(d,k,a,b):
    if k not in d:
        d[k] = [0,0,0,0,0]
    d[k][0] += 1                       #счетчик
    d[k][1] += a > b                   #победы
    d[k][2] += a == b                  #ничьи
    d[k][3] += a < b                   #поражения
    d[k][4] += 3 * (a > b) + (a == b)  #общий счет

for i in range(int(input())):
    a = input().split(';')
    add_r(r,a[0],a[1],a[3])
    add_r(r,a[2],a[3],a[1])

for i in r:
    print(i+':',*r[i])

============================================================

def points_counter(team, goals1, goals2):
    if team not in teams:
        teams[team] = [0] * 5
    teams[team][0] += 1
    teams[team][1] += int(goals1 > goals2)
    teams[team][2] += int(goals1 == goals2)
    teams[team][3] += int(goals1 < goals2)
    teams[team][4] += int(goals1 > goals2) * 3 + int(goals1 == goals2)


teams = dict()

for _ in range(int(input())):
    k = input().split(';')
    points_counter(k[0], int(k[1]), int(k[3]))
    points_counter(k[2], int(k[3]), int(k[1]))

for el in teams:
    print('{}:{} {} {} {} {}'.format(el, *teams[el]))
    
#or
for k, v in teams.items():
    print(k + ":" + str(v[0]), v[1], v[2], v[3], v[4])


============================================================
def edit(d, name, first, second):
    d[name][0] += 1
    d[name][1] += (first > second)
    d[name][2] += (first == second)
    d[name][3] += (first < second)
    d[name][4] += (first > second)*3 + (first == second)

d = {}
for i in range(int(input())):
    in_list = input().split(';')
    if in_list[0] not in d:
        d[in_list[0]] = [0]*5
    if in_list[2] not in d:
        d[in_list[2]] = [0]*5
    edit(d, in_list[0], int(in_list[1]), int(in_list[3]))
    edit(d, in_list[2], int(in_list[3]), int(in_list[1]))

[print(i[0], ":%d %d %d %d %d" %tuple(i[1]), sep='') for i in d.items()]

============================================================
a=[input().split(';') for i in range(int(input()))]
b={i:[] for i in set([i[0] for i in a])|set([i[2] for i in a])}
for i in a:
	b[i[0]].append(1 if i[1]==i[3] else 3 if i[1]>i[3] else 0)
	b[i[2]].append(1 if i[1]==i[3] else 3 if i[1]<i[3] else 0)
for i in b: print('%s:%i %i %i %i %i'%(i,len(b[i]),b[i].count(3),b[i].count(1),b[i].count(0),sum(b[i])))

Генератор словаря.
В классическом виде можно переписать так:
b={}
for i in set([i[0] for i in a])|set([i[2] for i in a]):
 b[i]=[]
set - множество - список неповторяющихся элементов.
| - объединение двух множеств. Множество неповторяющихся элементов первого и второго списка.
Т.е. формируем список команд из первого столбца [i[0] for i in a]. Тут могут быть повторения. 
Избавляемся от повторений преобразуя список в множество set([i[0] for i in a]). 
Тоже самое делаем для 3 столбца. Далее составляем множество из всех возможных 
названий команд первого и третьего столбца: set([i[0] for i in a])|set([i[2] for i in a]). 
Далее формируем словарь, где каждому названию команды ставим в соответствие пустой список:
b={i:[] for i in set([i[0] for i in a])|set([i[2] for i in a])}
Далее каждой команде добалвяем в список 3 балла за победу, 1 за ничью строки и 0 за поражение строки 2-5.
Потом для каждой команды считаем количество элементов в списке (количество игр), количество 
троек (выигрыши), количество 1 (ничьи), количество (0) - проигрыши и сумму элементов 
списка (сумму очков) и выводим на экран  - 6 строка.

or - работает с множеством как единым целым. | работает с элементами множества. 
Может этот пример прояснит Вам разницу:
a={1,2,3}
b={3,4,5}
c={}
print(c or b)
print(a or b)
print(a | b)
============================================================
d = {}
for a, p, b, v in (input().split(';') for n in range(int(input()))):
    d[a] = [i + j for i, j in zip(d.setdefault(a, [0, 0, 0, 0, 0]), [1, (p > v), (p == v), (p < v), 3 if p > v else (p == v)])]
    d[b] = [i + j for i, j in zip(d.setdefault(b, [0, 0, 0, 0, 0]), [1, (p < v), (p == v), (p > v), 3 if p < v else (p == v)])]
print(*(i+":" + ' '.join(map(str, d.get(i))) for i in d), sep='\n')

1. (в данном случае) zip по очереди возвращает пару элементов двух массивов с одинаковым индексом.

Например, это команда свою первую игру (вызов d.setdefault вернул [0,0,0,0,0]) 
выиграла (второе выражение дало [1,1,0,0,3]). Тогда zip даст пары: (0,1),(0,1),(0,0),(0,0),(0,3) 
и эти пары можно сложить.

2. Процитирую встроенную справку языка (выполните в интерактивном режиме python команду help(dict.get)):

D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.

Т.е. при обращении по отсутствующему в словаре ключу мы получим специальное значение None, 
а не выброс исключения KeyError. Это часто полезно, но бессмыслено в данном случае, 
когда ключи словаря перебираются явным образом.

============================================================
"""