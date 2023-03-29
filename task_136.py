#136. Подорожуючи на автомобілі, ви заїхали на автозаправну станцію. До наступної заправки 200 кілометрів. 
#Напишіть програму, яка буде визначати, чи потрібно вам заправлятися або ж можна почекати до наступної станції. 
#Програма повинна запитати: який розмір вашого бензобаку в літрах; скільки пального в бензобаку (у відсотках); 
#скільки кілометрів проходить автомобіль на одному літрі палива. Результатом роботи програми має бути інформація 
#про кількість кілометрів, які ще можна проїхати і почекати до наступної автозаправної станції, або негайно 
#заправитись.


S = 200 
tank = int(input('Enter your tank value: '))
fuel_capacity = int(input('Enter your quantity of fuel in tank: '))
route_per_liter = int(input('Enter how many km you can drive on 1 liter of fuel: '))

fuel = tank * (fuel_capacity/100)
range = fuel * route_per_liter
print(f'You can drive another {range} kilometers.')
print(f'Next refueling after {S} kilometers.')
if range > S:
    pass
else:
    print('FILL IN NOW!')