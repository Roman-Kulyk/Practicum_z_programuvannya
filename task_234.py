# 234. Система відслідковування помилок в комп’ютерній програмі збирає помилки щодня протягом n днів. 
# Напишіть програму, яка знаходить загальну кількість помилок, зібраних протягом n днів. 
# Користувач вводить кількість днів роботи системи відслідковування помилок n 
# і вводить кількість помилок m щодня (n і m - цілі числа).


n = int(input("Enter a number: "))
num_list = []
for i in range(0,n):
    m = int(input("Enter a number: "))
    num_list.append(m)
print(sum(num_list))


