# 385. Дано рядок, що є параграфом в тексті. Текст необхідно відформатувати так, 
# щоб довжина кожного рядка не перевищувала числа m, слова при цьому не розривати. 
# На вхід програмі спочатку подається число m (0 < m ≤ 255). У наступному рядку 
# знаходиться вхідний текст. Довжина слів в ньому не перевищує m, слова розділені 
# одним пропуском. Виведіть розбиття цього тексту на рядки довжиною не більше 
# ніж m символів (слово переноситься на наступний рядок тільки якщо в поточному рядку 
# його розмістити вже неможливо). Новий рядок не повинен починатися з пропуску.
'''
Вхідні дані:
10
The Wonderful Wizard of Oz

Вихідні дані:
The
Wonderful
Wizard of
Oz
'''