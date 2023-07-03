# 529. Створіть словник для зберігання інформації про міста. Використайте назви міст 
# в якості ключів словника. Створіть словник з інформацією про кожне місто: включіть в 
# нього країну, в якій розташоване місто, приблизну чисельність населення і один 
# цікавий факт про місто. Виведіть назву кожного міста і всю збережену інформацію про 
# нього як у вихідних даних.
'''
Вхідні дані:
Немає

Вихідні дані:
Rome:
	Country: Italy
	Population: 2868000 people
	Fact: Rome is one of the oldest cities in the world, the capital of Ancient Rome. Therefore, Rome is often called the "eternal city".
Canberra:
	Country: Australia
	Population: 381448 people
	Fact: The design of Canberra was based on the concept of a garden city.
Toronto:
	Country: Canada
	Population: 2503281 people
	Fact: In the world of professional sports, the city is the most famous hockey team of Toronto Maple Leafs. The city holds the nickname of the "hockey universe center".
'''
dictionary = {'Rome':
              [{'Country':'Italy'},
               {'Population':'2868000 people'},
               {'Fact':'Rome is one of the oldest cities in the world, the capital of Ancient Rome.'}],
              'Canberra':
              [{'Country':'Australia'},
               {'Population':'381448 people'},
               {'Fact':'The design of Canberra was based on the concept of a garden city.'}],
              'Toronto':
              [{'Country':'Canada'},
               {'Population':'2503281 people'},
               {'Fact':'In the world of professional sports, the city is the most famous hockey team'},]}
for key, value in dictionary.items():
    print(key, value,sep='\n')
    

'''for key, value in nba_teams.items():
    print(f"{key}:{value[0]} {value[1]} {value[2]} {value[3]} {value[4]}")'''