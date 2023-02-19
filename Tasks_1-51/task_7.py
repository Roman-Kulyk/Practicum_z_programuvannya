#Напишіть програму, яка друкує на екрані наступне повідомлення: Hello, Starlink
#subscriber! Your current balance is 125.56 UAH. Назва стільникової мережі і
#значення балансу вводиться з клавіатури.

network = input('Enter your network name:')
balance = int(input('Enter your balance:'))

print(f'Hello, {network} subscriber! Your balance is {balance:.2f} UAH. ')
