# 509. Ви створюєте пригодницьку гру і використовуєте для зберігання предметів 
# гравця словник, у якому ключі - це назви предметів, значення - кількість одиниць 
# кожної із речей. Виведіть повідомлення про усі речі гравця як у вихідних даних.
'''
Вхідні дані:
Немає

Вихідні дані:
Equipment:
3 key
1 mace
24 gold coin
1 lantern
10 stone
Total number of things: 39
'''
dictionary = {'key':3,\
              'mace':1,\
              'gold coin':24,\
              'lantern':1,\
              'stone':10}
for keys, values in dictionary.items():
    print(keys,':',values)
total_number = list(dictionary.values())

print('Total number of things: ',sum(total_number))