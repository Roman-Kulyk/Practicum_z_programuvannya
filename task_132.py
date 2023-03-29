#132. Дано ціле число n (1 ≤ n ≤ 4), яке визначає пору року: весна, літо, осінь, зима. 
#За вказаним значенням n необхідно надрукувати перелік місяців, які відносяться до цієї пори року.

n = int(input('Enter a number 1 =< n =< 4:'))
if n == 1:
    print("This is spring and months are: March, April and May")
elif n == 2:
    print("This is summer and mothns are: June, July and August")
elif n == 3:
    print('This is autumn and months are: September, October and November')
elif n == 4:
    print('This is winter and months are: December, January and February')
else:
    print('Incorrect data!')