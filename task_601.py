# 601. Кожен з n школярів деякої школи знає m мов. Визначте, які мови знають всі школярі і 
# мови, які знає хоча б один з школярів. Перший рядок вхідних даних містить кількість школярів n. 
# Далі йде n чисел m, після кожного з чисел йде m рядків, що містять назви мов, які знає i-й 
# школяр. Довжина назв мов не перевищує 1000 символів, кількість різних мов не більше 
# 1000 (1 ≤ n ≤ 1000, 1 ≤ m ≤ 500). У першому рядку виведіть кількість мов, які знають усі 
# школярі. Починаючи з другого рядка - список таких мов. Потім - кількість мов, які знає хоча 
# б один школяр, на наступних рядках - список таких мов.
"""
Вхідні дані:
3
3
Ukrainian
English
Polish
2
Ukrainian
English
1
English

Вихідні дані:
1
English
3
English
Polish
Ukrainian
"""
n = int(input("Enter amount of pupils: "))
languages_all = set(input().split()[1:])
languages_any = set(languages_all)

for _ in range(n -1):
    student_languages = set(input().split()[1:])
    languages_all &= student_languages
    languages_any |= student_languages

print(len(languages_all))
print(*languages_all, sep = '\n')
print(len(languages_any))
print(*languages_any, sep='\n')