# 643. Напишіть функцію, щоб вилучити певні символи із введеного рядка. 
# Спочатку вводиться початковий рядок, а далі з нового рядка символи, 
# які необхідно вилучити з початкового рядка. 
# Результатом має бути новий рядок без вилучених символів.
'''
Вхідні дані:
I did, did I?
d ?

Вихідні дані:
I i, i I
'''
def remove_chars(input_string, chars_to_remove):
     for char in chars_to_remove:
         input_string = input_string.replace(char, '')
         return input_string
    
     original_string = input("Enter a string: ")
     chars_to_remove = input("Enter chars to remove: ")

     result_string = remove_chars(original_string, chars_to_remove)
     print("Result:", result_string)

     remove_chars(input_string, chars_to_remove)

print(remove_chars('I did, did I?','d?'))