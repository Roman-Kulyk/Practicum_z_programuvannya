# Зчитайте цілі числа, які вводить користувач, по одному числу у рядку. Для кожного 
# введеного числа виконайте перевірку: якщо число менше 10, то пропускаємо це число, 
# якщо число більше 100, то припиняємо зчитувати числа. У інших випадках вивести це 
# число в окремому рядку.


while  True:
    num = int(input("Enter your number: "))
    if 10 < num < 100:
        print(num)
    elif num < 10:
        continue
    elif num > 100:
        break
