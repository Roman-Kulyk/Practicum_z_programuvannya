# 381. Капітан Флінт закопав скарб на Острові скарбів. Він залишив опис, як знайти 
# скарб. Опис складається з рядків виду: North 5, де перше слово - одне з North, 
# South, East, West, а друге число - кількість кроків, яку потрібно пройти в цьому 
# напрямку. Напишіть програму, яка за описом шляху до скарбу визначає точні координати 
# скарбу, вважаючи, що початок координат знаходиться на початку шляху, вісь OX 
# спрямована на схід, вісь OY - на північ. Програма отримує на вхід послідовність 
# рядків зазначеного виду, а введення завершується рядком зі словом Treasure!. 
# Програма має вивести два цілих числа в один рядок з пропуском між ними - координати 
# скарбу.
'''
Вхідні дані:
North 5
East 3
South 1
Treasure!

Вихідні дані:
3 4
'''
vertical = 0
horizontal = 0
while True:
    txt = input("Enter a direction: ")
    if txt.startswith("North"):
        vertical += int(txt[-1])
        
    elif txt.startswith("South"):
        vertical -= int(txt[-1])
        
    elif txt.startswith("East"):
        horizontal += int(txt[-1])
        
    elif txt.startswith("West"):
        horizontal -= int(txt[-1]),
           
    elif txt == "Treasure!":
        print(horizontal,vertical)
        break
