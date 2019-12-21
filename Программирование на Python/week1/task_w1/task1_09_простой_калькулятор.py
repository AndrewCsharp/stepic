"""
Напишите простой калькулятор, который считывает с пользовательского
ввода три строки: первое число, второе число и операцию, после чего применяет
операцию к введённым числам ("первое число" "операция" "второе число")
и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа.

Sample Input 1:
5.0
0.0
mod
Sample Output 1:
Деление на 0!

Sample Input 2:
-12.0
-8.0
*
Sample Output 2:
96.0

Sample Input 3:
5.0
10.0
/
Sample Output 3:
0.5
"""

a = float(input())
b = float(input())
operation = input()

result = None

if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '/':
    if b != 0:
        result = a / b
    else:
        result = 'Деление на 0!'
elif operation == '*':
    result = a * b
elif operation == 'mod':
    if b != 0:
        result = a % b
    else:
        result = 'Деление на 0!'
elif operation == 'pow':
    result = a ** b
elif operation == 'div':
    if b != 0:
        result = a // b
    else:
        result = 'Деление на 0!'
else:
    result = 'операция не определена'

print(result)


'''
x, y, operation = input(), input(), input().lower()

res = None

try:
    x = float(x)
    y = float(y)
except ValueError:
    print("Некорректные данные")
    exit()

if y == 0.0 and operation in ["/", "mod", "div"]:
    res = "Деление на 0!"
elif operation == "+":
    res = x + y
elif operation == "-":
    res = x - y
elif operation == "/":
    res = x / y
elif operation == "*":
    res = x * y
elif operation == "mod":
    res = x % y
elif operation == "pow":
    res = x ** y
elif operation == "div":
    res = x // y
else:
    res = "операция не определена"

print(res)

'''
