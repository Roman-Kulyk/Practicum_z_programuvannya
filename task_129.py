#129. Книжковий інтернет-магазин має книжковий клуб, який нараховує бали своїм клієнтам на основі кількості книг, 
#що купуються щомісяця (бали можна використати як знижку при черговому придбанні книги). 
#Бали нараховуються таким чином: якщо клієнт купує менше 2 книг, він отримує 0 балів; 
#якщо клієнт купує від 2 книг до 4 книг, він отримує 5 балів; якщо клієнт купує від 4 книг і до 6 книг, 
#він заробляє 15 балів; якщо клієнт купує від 6 книг до 8 книг, він заробляє 30 балів; 
#якщо клієнт купує 8 і більше книг, він заробляє 60 балів. Напишіть програму, 
#яка просить користувача ввести кількість книг, які він придбав у цьому місяці, 
#і відображає кількість отриманих балів.

book = int(input("Enter a q-ty of book you've bought in shop: "))

if book < 2:
    print('You have O points')
elif 2 <= book < 4:
    print('You have 5 points')
elif 4 <= book < 6:
    print('You have 15 points')
elif 6 <= book < 8:
    print('You have 30 points')
else:
    print('You have 60 points')