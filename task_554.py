# 554.Дано словник, в якому ключами є ідентифікатори абітурієнтів у форматі S x: 
# літера S, пропуски, x - порядковий номер абітурієнта, а значеннями - список назв 
# навчальних предметів, з яких абітурієнт буде здавати екзамен. 
# Напишіть програму для друку створеного словника і словника, в якому видалені 
# пропуски із ключів.
'''
Вхідні дані:
Немає

Вихідні дані:
{'S  001': ['Math', 'Computer Science'], 'S   002': ['Math', 'English'], 'S   003': ['Philosophy', 'English', 'Physical training']}
{'S001': ['Math', 'Computer Science'], 'S002': ['Math', 'English'], 'S003': ['Philosophy', 'English', 'Physical training']}
'''
dictionary = {'S  001': ['Math', 'Computer Science'], 
              'S   002': ['Math', 'English'], 
              'S   003': ['Philosophy', 'English', 'Physical training']}

print(dictionary)

# removing spaces from keys
# storing them in same dictionary
dictionary = {x.replace(" ",""):v
              for x,v in dictionary.items()}

# printing new dictionary
print(dictionary)

