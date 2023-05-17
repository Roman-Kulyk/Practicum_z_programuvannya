# 338. У рядку є кілька слів, розділених одним або декількома пропусками. 
# Потрібно прибрати з тексту зайві пропуски: два і більше пропусків поспіль, 
# а також всі пропуски на початку і в кінці рядка. На вхід програмі подається рядок, 
# що складається не більше ніж з 255 символів. Надрукувати новий рядок.
'''
Вхідні дані:

   Beyond the green     swelling hills of the     Mittel Land rose mighty slopes of forest    up    to the lofty steeps of the Carpathians    themselves

Вихідні дані:

Beyond the green swelling hills of the Mittel Land rose mighty slopes of forest up to the lofty steeps of the Carpathians themselves

'''
sample_input = input("Enter your txt: ")
sample_input = sample_input.strip()#The strip() method removes any leading 
# (spaces at the beginning) and trailing (spaces at the end) characters 
# (space is the default leading character to remove)
print(sample_input)
new_input = " ".join(sample_input.split())# join()-this method takes all items in 
# an iterable and joins them into one string.
print(sample_input.split())#The split() method splits a string into a list.
print(new_input)