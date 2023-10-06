# 815. Змоделюйте облік користувачів на сайті.Створіть клас з ім’ям User. 
# Створіть два атрибути first_name і last_name, а потім ще кілька атрибутів, які зазвичай 
# зберігаються у профілі користувача. Напишіть метод describe_user який виводить повне 
# ім’я користувача. Створіть ще один метод greeting_user() для виведення персонального 
#вітання для користувача. Викличте обидва методи для користувача.

# Додайте атрибут login_attempts (спроби входу в обліковий запис) у клас User. Напишіть 
# метод increment_login_attempts(), що збільшує значення login_attempts на 1. Напишіть 
# інший метод з ім’ям reset_login_attempts(), обнуляє значення login_attempts. Створіть 
# екземпляр класу User і викличте increment_login_attempts() кілька разів. Виведіть 
# значення login_attempts, щоб переконатися у тому, що значення було змінено правильно, а 
# потім викличте reset_login_attempts(). Знову виведіть login_attempts і переконайтеся у 
# тому, що значення обнулилося.

# Адміністратор - особливий різновид користувача. Напишіть клас з ім’ям Admin, що 
# успадковує від класу User. Додайте атрибут privileges для зберігання списку рядків виду 
# «Allowed to add message», «Allowed to delete users», «Allowed to ban users» і т. д. 

# Напишіть клас Privileges. Клас повинен містити всього один атрибут privileges зі списком,
# який треба забрати із класу Admin. Водночас, необхідно перемістити метод show_privileges()
#  у клас Privileges із класу Admin. Створіть екземпляр priv як атрибут класу Admin. 
#Створіть новий екземпляр класу Admin і використайте метод для виведення списку привілеїв.

# Додатково. Збережіть клас User в одному модулі, а класи Privileges і Admin у іншому 
# модулі. В окремому файлі створіть екземпляр класу Admin і викличте метод show_privileges(), 
# щоб перевірити, що все працює вірно.
# У вихідних даних наведений можливий варіант результатів виконання завдань.
"""
)
Bilbo Baggins
Hello, Bilbo Baggins
b)
3
0
c), d)
Allowed to add message
Allowed to delete users
Allowed to ban users
"""
class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.logging_attempts = 0

    def describe_user(self):
        print(f"User's name is: {self.first_name}")
        print(f"User's last name is: {self.last_name}")

    def greeting_user(self):
        print(f"Hello {self.first_name} {self.last_name}, nice to see you again!")
    
    def increment_login_attempts(self):
        self.logging_attempts = self.logging_attempts + 1
        print(f"This user has tried to loggin to the system {self.logging_attempts} times.")
    
    def reset_login_attempts(self):
        self.logging_attempts = 0
        print(f"This user has tried to loggin to the system {self.logging_attempts} times.")

class Admin(User):
    def __init__(self):
        self.priveleges = ['Allowed to add message', 'Allowed to delete users', 'Allowed to ban users']
    
class Priveleges(Admin):
    def show_priveleges(self):
        for i in self.priveleges:
            print(i)


us_1 = User('R2','D2', 23)
us_1.describe_user()
us_1.greeting_user()
print(us_1.logging_attempts)
us_1.increment_login_attempts()
us_1.increment_login_attempts()
us_1.increment_login_attempts()
us_1.reset_login_attempts()

us_2 = User('C3','P0',34)
us_2.describe_user()
us_2.greeting_user()
priv = Priveleges()
priv.show_priveleges()