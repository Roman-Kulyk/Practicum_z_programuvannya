# 451. Напишіть програму, яка зчитує числа (по одному в рядку) до тих пір, поки 
# сума введених чисел не буде дорівнює 0 і відразу після цього виводить суму квадратів 
# всіх чисел. Гарантується, що в якийсь момент сума введених чисел дорівнюватиме 0, 
# після цього зчитування продовжувати не потрібно.
'''
Вхідні дані:
2
3
-6
1

Вихідні дані:
50
'''
sum = 0 #it initialize variable sum
squares_sum = 0 #it initialize variable squares_sum

while True:
    num = int(input("Enter your number: ")) #it allows to input the data
    sum  += num #it adds entered data to the variabe sum
    squares_sum += num**2 #it adds data with exponentiation by two

    if sum == 0: #it checks if sum variable equal to 0
        break #if so it break the while cycle
print(squares_sum) #and print summ of data

    
