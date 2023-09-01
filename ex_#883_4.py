# Функція replace() може використовуватися для заміни будь-якого слова у рядку іншим словом. 
#Прочитайте кожен рядок зі створеного у попередньому завданні файла learning_python.txt 
# і замініть слово Python назвою іншої мови, наприклад C при виведенні на екран.


with open('ex_#883_3_learning_python.txt', 'rt' ) as freading:
    lines = freading.readlines()

for line in lines:
    print(line.replace('Python you can',"Java you can't").rstrip())