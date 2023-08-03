# 663. Напишіть функцію, яка перевіряє, чи рядок є паліндром чи ні. Регістр літер, 
# пропуски і знаки пунктуації не враховувати. Примітка. Паліндром - це слово, фраза 
# або послідовність, яка читається так само як зліва направо, так і справа наліво.
'''
Вхідні дані:
Level
No 'x' in Nixon
"Was it a car or a cat I saw?"
A man, a plan, a canal, Panama!
palindrome

Вихідні дані:

True
True
True
True
False
'''
def if_palindrome():
    text = input("Enter your text: ")
    text_corrected = []
    for i in text.lower():
        
        if i.isalpha():
            text_corrected.append(i)
        
    if text_corrected == text_corrected[::-1]:
        print(True)
    else:
        print(False)


if_palindrome()