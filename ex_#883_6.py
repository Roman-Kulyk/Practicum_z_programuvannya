# Зайдіть на сайт Project Gutenberg’s і знайдіть кілька книг для аналізу. Завантажте текстові файли цих творів 
# або скопіюйте текст з браузера у текстовий файл на вашому комп’ютері. Напишіть програму, яка зчитує дані з 
# файла і визначає кількість входжень слова 'the' в кожному тексті незалежно від регістру. Для підрахунку 
# кількості входжень слова або виразу в рядок можна скористатися функцією count().


with open('ex_#883_6_Tom_Sawyer.txt', 'rt' ) as freading:
    lines = freading.read()

x = lines.lower().count("the")

print(x) 