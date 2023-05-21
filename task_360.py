# 360.Вводиться рядок. Необхідно видалити з нього всі пропуски. 
# Після цього визначити, чи є він паліндромом, тобто однаково пишеться як зліва 
# направо, так і справа наліво. Програма має вивести Yes, якщо слово є паліндромом,
# або No у протилежному випадку.
'''
Вхідні дані:
123          621
Never     odd   or        even

Вихідні дані:
No
Yes
'''
sample_input = input("Enter your txt: ")
sample_input = sample_input.strip()#The strip() method removes any leading 
# (spaces at the beginning) and trailing (spaces at the end) characters 
# (space is the default leading character to remove)
print(sample_input)
new_input = " ".join(sample_input.split())# join()-this method takes all items in 
# an iterable and joins them into one string.

if new_input[0:] == new_input[::-1]:
    print("Yes")
else:
    print("No")
