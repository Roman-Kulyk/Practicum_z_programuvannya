#60.Тетяна кожен день лягає спати рівно опівночі і нещодавно дізналась, що
#оптимальний час для її сну становить t хвилин. Тетяна хочепоставити собі
#будильник так, щоб він продзвенів рівно через t хвилин після півночі, однак
#для цього необхідно вказати час сигналу у форматі години і хвилини. Допоможіть
#Тані визначити, на який час завести будильник. Години і хвилини у виведенні
#програми повиннірозташовуватися на різних рядках.

t = int(input('Enter a time for sleep: '))
hours_1 = t//60
minutes_1 = t%60
print(hours_1)
print(minutes_1)
