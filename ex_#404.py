#404. Створіть список things, що містить три елементи: 'wallet', 'mirror', 'umbrella'. 
# Виведіть на екран той елемент у списку things, який має відношення до дощу, 
# написавши його з великої літери, а потім виведіть список. 
# Переведіть «дощовий» елемент списку things у верхній регістр цілком і виведіть список. 
# Видаліть річ, яка захищає від дощу, зі списку things, а потім виведіть список на екран.


things = ['wallet', 'mirror', 'umbrella']

print(things[-1].title())
print(things)
print(things[-1].upper())
print(things)
things.pop()
print(things)