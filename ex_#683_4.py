# Зчитайте ціле число введене користувачем і виведіть повідомлення про те, 
# чи число парне або непарне.
def if_even():
    num = int(input("Enter your number: "))
    if num % 2 ==  0:
        print('Even number')
    else:
        print('Odd number')

if_even()