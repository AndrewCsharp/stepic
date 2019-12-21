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

"""
====================================================

cntWords = int(input())
words = set()

for i in range(cntWords):
    words.add(input().lower())

cntSt = int(input())
st = list()

for i in range(cntSt):
    s = input().lower().split()
    for x in s:
        if (x not in words) and (x not in st):
            st.append(x)

print(*st, sep="\n")

====================================================

# формируем множество известных слов на основании построчного ввода
dic = {input().lower() for _ in range(int(input()))}

# заводим пустое множество для приема текста
wrd = set()

# т.к. текст построчно подается, а также в каждой строке несколько слов,
# то каждую строку превращаем во множество и добавляем в единое множество wrd
for _ in range(int(input())):
    wrd |= {i.lower() for i in input().split()}

# на вывод отправляем результат вычитания словарного множества dic
# из текстового множества wrd; впереди ставим *, чтобы раскрыть поэлементно
print(*(wrd-dic), sep="\n")

#Основа работы кода - свойство множеств хранить только уникальные значения.
#wrd |= {...} отвечает за добавление множества {...} в единое wrd (аналог метода update)
#Обращаем внимание на звездочку *, которая вытаскивает элементы на вывод, вместо того,
# чтобы печатать в виде множества
#заменил метод difference на оператор вычитания, чтобы добиться
# единообразия - использовать для действий с множествами либо операторы, либо методы,
# а не все одновременно

====================================================

know = {input().lower() for i in range(int(input()))}
new_text = []
for j in range(int(input())):
    new_text+=(input().lower().split())
for g in set(new_text) - know:
        print(g,end='\n')

====================================================
вариант решения: 
1) заполняем словарь; 
2) преобразуем текст в множество слов; 
3) печатаем разность двух множеств

words = set(input().lower() for i in range(int(input())))
text = set(('\n'.join(input().lower() for i in range(int(input())))).split())
print('\n'.join(text - words))

"""