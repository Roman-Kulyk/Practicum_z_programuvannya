# 311. Користувач вводить рядок і набір символів. 
# Напишіть програму, яка перевіряє чи починається рядок із зазначених символів.
'''
Вхідні дані:

wireless router
route

Вихідні дані:

False

'''
message_1 = input("Enter a message: ")
message_2 = input("Enter symbols: ")
if message_1.startswith(message_2):
    print(True)
else:
    print(False)