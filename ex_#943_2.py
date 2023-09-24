# Створіть об’єкт happy, що містить дату вашого народження. 
# Використайте функції для роботи з датою і часом, щоб дізнатися відповіді на такі питання 
# (виведення організуйте в окремий файл у вигляді, на зразок «запитання: відповідь», у окремих рядках):
# "Яка дата вашого народження?"
# "У який день тижня ви народилися?"
# "Коли вам буде (або вже було) 13 330 днів від народження?"
import datetime
happy = datetime.date(2005,7,29)#it creates an object with date

questions =["Яка дата вашого народження?",
            "У який день тижня ви народилися?",
            "Коли вам буде (або вже було) 13 330 днів від народження?"]

answers = [
    str(happy),
    happy.strftime("%A"),
    (happy + datetime.timedelta(days=13330)).strftime("%Y-%m-%d")
]

with open ('ex_#943_2_output.txt', 'w') as file:#it writes answers and questios in the output file
    for q,a in zip(questions,answers):
        file.write(f"{q}:{a}\n")