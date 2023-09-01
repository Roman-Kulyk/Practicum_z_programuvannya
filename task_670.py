# 670.Дано список кортежів, кожен з яких містить два значення: назва фільму (рядок) 
# і рейтинг (дійсне число). Напишіть функцію(ї) для сортування кортежів в порядку 
# зростання рейтингу.
'''
Вхідні дані:
Список із кортежів

Вихідні дані:
[('Captain Marvel', 7.0), ('Aladdin', 7.4), ('Toy Story 4', 8.2), ('Avengers: Endgame', 8.7)]
'''
def sort_tuples(tuples):
    sort_tuples = sorted(tuples, key=lambda x:x[1])
    #sort_tuples = sorted(tuples, key=None, reverse=False)
    
    return sort_tuples

films = [('Aladdin', 7.4),('Captain Marvel', 7.0),('Avengers: Endgame', 8.7),('Toy Story 4', 8.2)]
sorted_films = sort_tuples(films)
print(sorted_films)


sort_tuples(films)