#571. Напишіть програму, яка зможе підрахувати слова у введеному рядку, 
# розділені пропуском і вивести отриману статистику: для кожного унікального слова обчислити 
# число його повторень (без урахування регістру), слова не повинні повторюватися, 
# порядок слів довільний.
"""
Вхідні дані:
a bb acD bb abc ac BCD a

Вихідні дані:
a 2
bb 2
acd 1
abc 1
ac 1
bcd 1
"""
text = input("Enter your string: ").split()

string = []
for i in text:
    
    if i not in string:
        string.append(i.lower())
        print(i.lower(),text.count(i))
    else:
        continue