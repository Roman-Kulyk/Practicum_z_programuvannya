#401. Збережіть назви мов світу (Ukrainian, French, Bulgarian, Norwegian, Latvian або інші) у списку. 
# Простежте за тим, щоб елементи у списку не зберігались в алфавітному порядку. 
# Застосуйте функції sorted(), reverse(), sort() до списку. 
# Виведіть список на екран до і після використання кожної із функцій.


languages = ['Ukrainina','French','Bulgarian','Norwegian','Latvian']

languages.sort()
print(languages)
languages.reverse()
print(languages)
languages_sorted = sorted(languages)
print(languages_sorted)
print(languages)