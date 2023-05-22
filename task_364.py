# 364. Вводиться рядок. Потрібно видалити з нього повторювані символи і всі пропуски.
'''
Вхідні дані:
aa
a a b b c dd e

Вихідні дані:
a
abcde
'''
input_string = input("Enter a string: ")
unique_chars = []#it initialize empty list
for char in input_string:#it goes through every character in input_string
    if char not in unique_chars and char != " ":#and checks if the char in unique_chars list
        #and char is not space
        unique_chars.append(char)#it adds chars to the unique_char list
        output_string = "".join(unique_chars)#it turns list into a string
print(output_string)#it prints string