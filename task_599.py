# 599.На вхід програми подається рядок, який містить одне ціле число n - кількість англійських 
# слів у англійсько-латинському словнику, за якими йдуть n перекладів цих слів. 
# Кожен запис міститься в окремому рядку, що містить перше англійське слово, потім дефіс, 
# оточений пропусками, а потім розділений комами список з перекладами цього англійського слова 
# на латинській мові. Всі слова складаються лише з англійських літер. 
# Переклади сортуються в лексикографічному порядку. Порядок англійських слів у словнику також 
# лексикографічний. Надрукуйте відповідний латинсько-англійський словник у тому ж форматі 
# (кількість слів та їхні переклади). 
# Зокрема, першим у рядку слів має бути лексикографічно мінімальний переклад латинського слова, 
# потім другого в цьому порядку і т. д. 
# Англійські слова в кожному рядку також слід сортувати лексикографічно.
"""
Вхідні дані:
3
apple - malum, pomum, popula
fruit - baca, bacca, popum
punishment - malum, multa

Вихідні дані:
7
baca - fruit
bacca - fruit
malum - apple, punishment
multa - punishment
pomum - apple
popula - apple
popum - fruit
"""
num = int(input("Enter your nuber:"))
eng_lat_dict = {}
for _ in range(num):
    inquiry = input("Enter your word with translation: ").split(' - ')
    print(inquiry)
    eng_lat_dict[inquiry[0]] = inquiry[1:]
    print(eng_lat_dict)

# list out keys and values separately
key_list = list(eng_lat_dict.keys())
val_list = list(eng_lat_dict.values())
print(key_list)
print(val_list)

for val in eng_lat_dict:
    print()