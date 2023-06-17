# 481. У рядку через кому перераховані слова. Сформувати з цих слів новий рядок. 
# Слова мають бути відсортовані за спаданням (від Z до A) без урахування регістру і 
# записані через пропуск.
'''
Вхідні дані:
horse, cat, parrot, goldfish, dog

Вихідні дані:
parrot horse goldfish dog cat
'''
lst = input("Enter the list members: ").split(", ")
lst.sort(reverse=True)
message = " ".join(lst)
print(message)