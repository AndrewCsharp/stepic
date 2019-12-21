"""
Билет считается счастливым, если сумма первых трех цифр
совпадает с суммой последних трех цифр номера билета.

На вход программе подаётся строка из шести цифр.
Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.

Sample Input 1:
090234
Sample Output 1:
Счастливый

Sample Input 2:
123456
Sample Output 2:
Обычный

"""

bilet = input()

if int(bilet[0])+int(bilet[1])+int(bilet[2]) == int(bilet[3])+int(bilet[4])+int(bilet[5]):
    print('Счастливый')
else:
    print('Обычный')

"""

strNum = input()

sumL = 0
sumR = 0

for i in range(len(strNum)):
  if i < 3:
      sumL += int(strNum[i])
  else:
      sumR += int(strNum[i])

if sumL == sumR:
  print("Счастливый")
else:
  print("Обычный")

===========================================================================================

s = input()
print('Счастливый' if int(s[0])+int(s[1])+int(s[2]) == int(s[3])+int(s[4])+int(s[5]) else 'Обычный')

===========================================================================================
tiket = input()

half = len(tiket) // 2

rightHalf = sum(list(map(int, tiket[:half])))
leftHalf  = sum(list(map(int, tiket[half:])))

print("Счастливый" if rightHalf==leftHalf else "Обычный")

"""

