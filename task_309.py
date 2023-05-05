# 309. Дано рядок. Змініть регістр символів в цьому рядку так, 
# щоб перша буква кожного слова була великою, а інші літери - малими.
'''
Вхідні дані:

A scandal in Bohemia
The adventure of the Blue Carbuncle
The Boscombe valley mystery

Вихідні дані:

A Scandal In Bohemia
The Adventure Of The Blue Carbuncle
The Boscombe Valley Mystery

'''
message = 'A scandal in Bohemia\nThe adventure of the Blue Carbuncle\nThe Boscombe valley mystery'
print(message.title())