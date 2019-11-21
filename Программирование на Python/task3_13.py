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
