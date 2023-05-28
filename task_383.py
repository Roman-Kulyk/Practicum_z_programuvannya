# 383. Напишіть програму для друку літери A за допомогою введеного користувачем символа.
'''
Вхідні дані:
*

Вихідні дані:
  ***
 *   *
 *   *
 *****
 *   *
 *   *
 *   *
'''
char = input("Enter your character: ")
print(" "+char*3+"")
print(char+" "*3 +char)
print(char+" "*3 +char)
print(char*5)
print(char+" "*3 +char)
print(char+" "*3 +char)
print(char+" "*3 +char)