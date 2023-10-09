# 819. Напишіть клас Dog, який має три атрибути класу: mammal (ссавець), nature (характер) і 
# breed (порода), та два атрибути ексземпляра: name (кличка) і age (вік). 
# Створіть екземпляри трьох нових собак, кожна з яких різного віку. 
# Визначте у класі Dog метод для виведення значень атрибутів екземпляру - імені та віку 
# конкретної собаки. 
# За потреби, додайте кілька інших методів, які визначають поведінку собаки (подавання голосу 
# тощо). 
# Напишіть кілька класів, які унаслідуються від батьківського класу Dog, що описують конкретні 
# породи собак. 
# Визначте для цих класів атрибути nature і breed відповідно, включіть у класи по одному 
# методу, що визначає поведінку конкретної породи собаки. 
# Створіть батьківський клас Pets, що створює список ваших домашніх улюбленців. 
#У підсумку, надрукуйте інформацію про ваших домашніх тварин, на зразок, як у вихідних даних.
"""
Вхідні дані:
Немає

Вихідні дані:
I have 3 dogs.
Toby is 4. Kind Golden Retriever breed dog.
Charlie is 6. Tireless Jack Russell Terrier breed dog.
Rocky is 7. Obedient ordinary breed dog.
And they're all mammals, of course.
"""

class Dog():
    mammal = True
    nature = 'loyal'
    breed = None
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_barking(self):
        print(f"{self.name} is barking: Guvh! Guvh!!!")
    
    def get_attributes(self):
        print(f"Dog's name is {self.name} and it is {self.age} year's old.")

dog_1 = Dog('Oskar',2)
dog_1.breed = 'Terier'
dog_2 = Dog('Topic',3)
dog_2.breed = 'Dvor Terier'
dog_3 = Dog('Gerda',4)
dog_3.breed = 'German Sheppard'
print(f"{dog_1.name} is {dog_1.breed};")
print(f"{dog_2.name} is {dog_2.breed};")
print(f"{dog_3.name} is {dog_3.breed}.")

dog_1.get_attributes()
dog_2.get_attributes()
dog_3.get_attributes()

dog_1.get_barking()
dog_2.get_barking()
dog_3.get_barking()
