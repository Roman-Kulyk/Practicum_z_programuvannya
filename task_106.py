# 106. Напишіть програму, в якій користувач вводить значення температури, і, 
#якщо це значення менше або дорівнює 0 градусів Цельсія, необхідно вивести повідомлення A cold, isn’t it?. 
#Якщо ж температура становить більше 0 і менше 10 градусів Цельсія повідомлення буде Cool., 
#у інших випадках Nice weather we’re having..

temperature = float(input('Enter a value: '))
if temperature <= 0:
    print('A cold isn\'t it?')
elif 0 < temperature < 10:
    print('Cool.')
else:
    print('Nice weather we\'re having.')