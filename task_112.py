# 112. Напишіть програму, на вхід якої подається два цілих числа - вік Сашка і вік Тетянки. 
#Програма має вивести повідомлення про те, хто є старшим серед них.

num_1 = int(input('Enter a first value: '))
num_2 = int(input('Enter a second value: '))

if num_1 > num_2:
    print('Sasha is older than Tanya.')
else:
    print('Tanya is older than Sasha.')
