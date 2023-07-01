# 524.Словники можуть використовуватися для моделювання справжнього словника. 
# Оберіть кілька термінів з програмування (або із іншої області), які ви знаєте на 
# цей момент. Використайте ці слова як ключі словника, а їх визначення - як значення. 
# Виведіть кожне слово і його визначення у спеціально відформатованому вигляді як у 
# вихідних даних.
'''
Вхідні дані:
Немає

Вихідні дані:
variable
	a symbolic name associated with a value and whose associated value may be changed
type
	is a classification of data which tells the compiler or interpreter how the programmer intends to use the data
program
	a collection of instructions that performs a specific task when executed by a computer
'''
dictionary = {'variable':'\ta symbolic name associated with a value and whose associated value may be changed',\
              'type':'\tis a classification of data which tells the compiler or interpreter how the programmer intends to use the data program',\
              'program':'\ta collection of instructions that performs a specific task when executed by a computer'}
for key, value in dictionary.items():
    print(key,value, sep='\n')