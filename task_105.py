#105.Користувач вводить дві різних англійські літери в окремих рядках. 
#Напишіть програму, яка виводить повідомлення про місце розташування однієї літери відносно іншої у алфавіті.

let_1 = tuple(input('Enter a first letter: '))
let_2 = tuple(input('Enter a second letter: '))
alphabet = 'abcdefghijklmnopqrstuvwxyz'
if let_1[0] < let_2[0]:
    print(str(let_1) + ' is earlier in alphabet.')
else:
    print(str(let_2) + ' is earlier in alphabet.')