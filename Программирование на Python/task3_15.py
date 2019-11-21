"""
Простейшая система проверки орфографии основана на использовании списка
известных слов. Каждое слово в проверяемом тексте ищется в этом списке и,
если такое слово не найдено, оно помечается, как ошибочное.

Напишем подобную систему.

Через стандартный ввод подаётся следующая структура: первой строкой — количество d
записей в списке известных слов, после передаётся  d строк с одним словарным
словом на строку, затем — количество l строк текста, после чего — l строк текста.

Напишите программу, которая выводит слова из текста, которые не встречаются в словаре.
Регистр слов не учитывается. Порядок вывода слов произвольный.
Слова, не встречающиеся в словаре, не должны повторяться в выводе программы.

﻿
Sample Input:
3
a
bb
cCc
2
a bb aab aba ccc
c bb aaa

Sample Output:
aab
aba
c
aaa

"""
cntWords =  int(input())
listWords = []
for i in range(cntWords):
    word = input()
    listWords.append(word.lower())

cntStreeng =  int(input())
stringText=[]
for i in range(cntStreeng):
    text = input().lower().split()
    stringText += text

notFoundWords=[]
for s in stringText:
    if s not in listWords:
        notFoundWords.append(s)

notFoundWords = list(set( notFoundWords))
for s in notFoundWords:
    print(s)
