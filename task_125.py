#125.Напишіть програму, яка просить користувача ввести вік людини (ціле число). 
#Програма повинна вивести повідомлення про те, чи є особа немовлям, дитиною, 
#підлітком або дорослим за такими правилами: якщо людині 1 рік або менше, він або вона є немовлям, 
#якщо особа старше 1 року, але молодше 13 років, вона є дитиною, якщо особа не молодше 13 років, 
#але молодше 20 років, вона є підлітком і якщо особа віком старше 20 років, вона є дорослою.

age = int(input('Enter an age: '))
if age <= 1:
    print('You are todler')
elif 1 < age < 13:
    print('You are child')
elif 13 <= age < 20:
    print('You are an adult')
else:
    print('You are a MAN')