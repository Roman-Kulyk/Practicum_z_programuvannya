# 817. Напишіть клас Car, який надає для створених екземплярів такі атрибути даних 
# автомобіля: марку виготовлення автомобіля, модель автомобіля, рік автомобіля, швидкість 
# (початкове значення 0). Клас також повинен мати наступні методи: accelerate (метод 
# повинен щоразу додавати 5 до значення атрибуту даних про швидкість), brake (метод повинен 
# віднімати 5 від значення атрибута даних швидкості кожного разу, коли він викликається), 
# get_speed (метод повинен повернути поточну швидкість). Створіть екземпляр класу Car і 
# викличте метод accelerate п’ять разів. Після кожного виклику методу accelerate отримайте 
# поточну швидкість автомобіля і надрукуйте її значення. Потім викличте метод brake п’ять 
# разів. Після кожного виклику методу brake отримайте поточну швидкість автомобіля та 
# надрукуйте її значення.
class Car():
    def __init__(self, model, mark, year, speed = 0):
        self.model = model
        self.mark = mark
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed = self.speed + 5

    def brake(self):
        self.speed = self.speed - 5
    
    def get_speed(self):
        print(f"current speed is {self.speed}")

car1 = Car('BMW','3M', 2023)
print('Car accelerates:')
for i in range(5):
    car1.accelerate()
    car1.get_speed()
print("Car brakes:")
for i in range(5):
    car1.brake()
    car1.get_speed()
print("Car stopped.")
