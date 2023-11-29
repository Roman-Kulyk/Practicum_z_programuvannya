# 604. Вводиться число n, за яким слідують n рядків тексту. Напишіть програму, яка друкує всі 
# слова, що зустрічаються в тексті, по одному на рядок, і їхню кількість входжень у текст. Слова 
# повинні бути відсортовані в порядку спадання відповідно до їх кількості, і всі слова при 
# однаковому числі входжень у текст повинні бути надруковані в лексикографічному порядку. 
# Вказівка. Після того, як ви створите словник усіх слів, вам захочеться впорядкувати його по 
# частоті слова. Бажаного можна домогтися, якщо створити список, елементами якого будуть кортежі 
# з двох елементів: частота зустрічальності слова і саме слово. 
# Наприклад, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тоді стандартне сортування буде сортувати 
# список кортежів, при цьому кортежі порівнюються по першому елементу, а якщо ці елементи рівні - 
# то по другому.
"""
Вхідні дані:
9
hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme

Вихідні дані:
damme 4
is 3
name 3
van 3
bond 2
claude 2
hi 2
my 2
james 1
jean 1
what 1
your 1
"""
n = int(input("Enter your number: "))
text = ''
for i in range(n):
    
    row = input("Enter your row: ")
    text += row +' '

text_list = text.split()

# Python code to convert dictionary into list of tuples
text_dict = {}# Initialization of dictionary
for i in text_list:
    if i not in text_dict:
        counter = text_list.count(i)
        text_dict[i] = counter


# Converting into list of tuple
#list = list(text_dict.items())

# Using zip
listt = zip(text_dict.values(), text_dict.keys())
 
# Converting from zip object to list object
listt = list(sorted(listt))

print(listt)
# Printing list of tuple
for i in listt:
    print(f'{i[0]} {i[1]}', sep= ' ')

