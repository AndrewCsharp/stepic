"""
Коля каждый день ложится спать ровно в полночь и недавно узнал,
что оптимальное время для его сна составляет X минут.
Коля хочет поставить себе будильник так, чтобы он прозвенел ровно через X минут
после полуночи, однако для этого необходимо указать время сигнала в формате часы, минуты.
Помогите Коле определить, на какое время завести будильник.

Часы и минуты в выводе программы должны располагаться на разных строках.

Sample Input 1:                 Sample Input 2:
480                             512
Sample Output 1:                Sample Output 2:
8                               8
0                               32

"""
x = int(input())
print(x // 60, x % 60, sep="\n")
