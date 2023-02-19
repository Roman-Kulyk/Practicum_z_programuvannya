#26.Напишіть програму, щоб конвертувати усі введені користувачем одиниці часу
#(дні, години, хвилини, секунди) в загальну кількість секунд.

num_1 = int(input('Enter days: '))
num_2 = int(input('Enter hours: '))
num_3 = int(input('Enter minutes: '))
num_4 = int(input('Enter seconds: '))



sum = num_1 * 60 *60 * 24 + num_2 * 60 * 60 + num_3 * 60 +num_4
print('The total amount of seconds: ',sum)
