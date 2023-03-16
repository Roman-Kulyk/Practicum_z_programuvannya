#111. Серед учнів школи проводилося тестування з трьох предметів, по кожному з яких учні отримали певну кількість 
#балів (цілі числа). Напишіть програму, яку можуть використати учні для обчислення їхнього середнього балу трьох 
#тестів і виведення середнього значення. Окрім того, необхідно передбачити виведення повідомлення Congratulations! 
#That is a great average!, якщо середній бал більший ніж 95.

num_1 = int(input('Enter a first value: '))
num_2 = int(input('Enter a second value: '))
num_3 = int(input('Enter a third value: '))

average = (num_1 + num_2 + num_3) // 3
print('Your average is ' + str(average))
if average > 95:
    print('Congratulations! That is a great average!')