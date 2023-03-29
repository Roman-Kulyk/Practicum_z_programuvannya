#124. Напишіть програму, яка запитує користувача номер в діапазоні від 1 до 7. 
#Програма повинна відображати відповідний день тижня, де 1 - це понеділок, а 7 - неділя. 
#Програма має враховувати варіант, коли користувач вводить номер, що знаходиться за межами діапазону від 1 до 7.
num = int(input('Enter a number from 1 to 7: '))
if num == 1:
    print('Monday')
elif num == 2:
    print('Tuesday')
elif num == 3:
    print('Wednesday')
elif num == 4:
    print('Thursday')
elif num == 5:
    print('Friday')
elif num == 6:
    print('Saturday')
else:
    print('Wrong number')