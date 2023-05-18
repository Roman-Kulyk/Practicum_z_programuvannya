# 349. Дано рядок, що складається з рівно двох слів, розділених пропуском. 
# Надрукуйте новий рядок, у якому позиції першого та другого слова змінені 
# (друге слово друкується спочатку). У завданні не можна використовувати цикли 
# і вказівку «якщо».
'''
Вхідні дані:
Linux Ubuntu
Richard Stallman
Вихідні дані:
Ubuntu Linux
Stallman Richard
'''
txt = input("Enter a string: ")
splited_txt = txt.split()
print(splited_txt[1],splited_txt[0])