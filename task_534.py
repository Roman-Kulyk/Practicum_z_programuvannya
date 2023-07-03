# 534. Змоделюйте аркуш елетронної таблиці на основі словника. Створіть порожній 
# словник для зберігання значень комірок аркушу електронної таблиці. Заповніть словник 
# кількома значеннями: в одному рядку вводиться адреса комірки у форматі A1, 
# де A - назва стовпця, 1 - номер рядка, і, через пропуск, значення, яке необхідно 
# зберегти в комірці. Надрукуйте «комірки» словника з їхніми значеннями.
'''
Вхідні дані:
A1 300
B1 2050
B2 Python

Вихідні дані:
('A', '1') 300
('B', '1') 2050
('B', '2') Python
'''
sheet = {}

sheet.update({"A1": 300})
sheet.update({"B1": 2050})
sheet.update({"B2": "Python"})

for key, value in sheet.items():
    print(tuple(key), value)