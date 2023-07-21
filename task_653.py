# 653. Напишіть функцію, яка приймає два списки та повертає True, якщо у них є 
# щонайменше один спільний елемент.
'''
Вхідні дані:
1 2 3 4 5
6 7 8 9 0
1 two three four five 6 seven 8 9 ten
five hundred

Вихідні дані:
False
True
'''
def vocab_func(text_1, text_2):
        
    for i in text_1:
        if i in text_2:
            return True
        
    return False
            
text_1 = input("Enter your list: ").split()
text_2 = input("Enter your list: ").split()

print(vocab_func(text_1,text_2))