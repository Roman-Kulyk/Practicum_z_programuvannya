#405. Поміркуйте над тим, яку інформацію можна було б зберігати у списку. Наприклад, створіть список 
# професій, видів спорту, членів родини, назви океанів тощо, а потім викличте кожну функцію для роботи зі 
# списками, яка була згадана у цьому розділі, хоча б один раз.


hobby = ['footbal', 'painting','sewing','hochey','music','dance']
print(len(hobby))
print(', '.join(hobby))
print(hobby[::-1])
print(hobby.index('dance'))
hobby[3] = 'yoga'
print(hobby)
hobby.append('hockey')
print(hobby)
del hobby[-2]
print(hobby)
hobby.pop()
print(hobby)
print('hockey' in hobby)
print('golf' not in hobby)
sorted_hobby = sorted(hobby)
print(sorted_hobby)
sorted_hobby.reverse()
print(sorted_hobby)