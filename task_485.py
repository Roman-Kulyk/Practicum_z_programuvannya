# 485. Суть завдання та ж, що і у задачі Шифр Цезаря, з однією відмінністю: кодуються 
# символи з інтервалу 1F600-1F64F таблиці символів Unicode. Використовується кодування UTF-8. 
# Для всіх символів зсув один і той же. Зсув циклічний, тобто, якщо до останнього символу 
# алфавіту застосувати одиничний зсув, то він заміниться на перший символ, і навпаки. 
# Напишіть програму, яка шифрує текст шифром Цезаря. На першому рядку вказується 
# використовуваний зсув шифрування: ціле число. Додатне число відповідає зсуву вправо. 
# На другому рядку вказується непорожня фраза для шифрування. Не звертайте уваги, якщо у 
# вас відображаються прямокутники замість деяких символів. Це означає, що ваш шрифт не 
# містить цих символів. Програма має вивести єдиний рядок, в якій записана зашифрована 
# послідовність.
"""
Вхідні дані:
2
😍😎😏

Вихідні дані:
😏😐😑
"""