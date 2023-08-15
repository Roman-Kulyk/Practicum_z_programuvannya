# 683. Напишіть функцію для виконання рядка, що містить код Python. Реалізуйте функцію разом 
# із конструкцією try/except, яка має відпрацювати як у вихідних даних.
'''
Вхідні дані:
print('Hello, World!')
print(36+51)
print(2 + 'a')

Вихідні дані:
Hello, World!
Successfully
Done
87
Successfully
Done
Not fulfilled
Done
'''
def execute_code(code):
    try:
        exec(code)
        print('Successfully')
        
    except Exception as e:
        print('Not fulfilled: ',e)
    print('Done')
code = "print(36+51)"
execute_code(code)