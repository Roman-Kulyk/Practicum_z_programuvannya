#Ви придбали товар на певну суму s. Скільки купюр різного номіналу треба віддати продавцю, якщо починати платити з 
#найбільших? У вас є 1, 2, 5, 10, 100, 500 гривень.

s = int(input('Enter a price: '))
five_hundred = s // 500
one_hundred = s % 500 // 100
ten = s % 100 // 10
five = s % 10 // 5
two = s % 5 // 2
one = s % 5 % 2 // 1 
print(f'(500) {five_hundred}, (100) {one_hundred}, (10) {ten}, (5) {five}, (2) {two}, (1) {one}'.format(five_hundred, one_hundred, ten, five, two, one))
