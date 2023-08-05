# 649. Напишіть функцію, яка отримує рядок і обчислює кількість великих та нижніх 
# букв в ньому і друкує результат як у вихідних даних - спочатку кількість великих, 
# а потім кількість малих літер.
'''
Вхідні дані:
Was it a car or a cat I saw?

Вихідні дані:
2
17
'''
def what_case(text):
    upper = []
    lower = []
    list_text  = list(text)
    for i in list_text:
        if i.isupper():
            upper.append(i)
        elif i.islower():
            lower.append(i)
    print(len(upper))
    print(len(lower))

what_case("Was it a car or a cat I saw?")