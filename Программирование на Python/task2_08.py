"""
students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']
students += 'Olga'
print(students)  # ['Ivan', 'Masha', 'Sasha', 'Olga', 'O', 'l', 'g', 'a']

============================================================================
Напишите программу, на вход которой подается одна строка с целыми числами. 
Программа должна вывести сумму этих чисел.

Используйте метод split строки.

Sample Input:
4 -1 9 3
Sample Output:
15
"""
a = [int(i) for i in input().split()]
print(sum(a))
