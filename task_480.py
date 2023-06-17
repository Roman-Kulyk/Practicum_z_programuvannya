# 480. Дано список назв міст світу, перерахованих в рядку через кому. 
# Сформуйте з елементів списку повідомлення, у якому перед останнім елементом буде 
# вставлено слово and так, як у вихідних даних. Програма має працювати з будь-якими 
# списками, які мають довільну довжину, відмінну від нуля.
'''
Вхідні дані:
Budapest, Rome, Istanbul, Sydney, Kyiv, Hong Kong
Kyiv, Hong Kong
Budapest

Вихідні дані:
Budapest, Rome, Istanbul, Sydney, Kyiv and Hong Kong
Kyiv and Hong Kong
Budapest
'''
lst = input("Enter the list members: ").split(", ")

message = ", ".join(lst[:-1]) + " and " + lst[-1]
print(message)