# 537. Дано список словників. Кожен словники має 2 пари елементів: 
# ключ name і значення імені студента, ключ points і значення - список балів з різних 
# дисциплін (цілі двоцифрові числа). Надрукуйте найменші значення балів, отримані 
# кожним студентом, в один рядок з пропуском.
'''
Вхідні дані:
Немає

Вихідні дані:
45 60 30 49
'''
list_of_dicts = [{"name_1":"Roman","points":[23,34,45,56,67,78]},
                 {"name_2":"Ivan","points":[11,22,33,44,55,66]},
                 {"name_3":"Stepan","points":[98,87,76,65,54,43]},
                 {"name_4":"Ignat","points":[54,34,55,34,65,65]}]


list_value_1 = list_of_dicts[0]["points"]
list_value_2 = list_of_dicts[1]["points"]
list_value_3 = list_of_dicts[2]["points"]
list_value_4 = list_of_dicts[3]["points"]

print(min(list_value_1),min(list_value_2),min(list_value_3),min(list_value_4))

