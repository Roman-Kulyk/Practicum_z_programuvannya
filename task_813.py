# 813. Змоделюйте роботу онлайн-магазину.
# Напишіть клас з ім’ям Shop(). Метод __init__() класу Shop() повинен містити два атрибути:
# shop_name і store_type. Створіть метод describe_shop(), який виводить два атрибути, 
# і метод open_shop(), який виводить повідомлення про те, що онлайн-магазин відкритий. 

 #Створіть на основі класу екземпляр з ім’ям store. 
 #Виведіть два атрибути окремо, потім викличте обидва методи.
 #Створіть ще один екземпляр класу, викличте для нього метод describe_shop().
 
#Додайте атрибут number_of_units зі значенням за замовчуванням 0; він представляє 
# кількість видів товару у магазині. Виведіть значення number_of_units, а потім змініть 
# number_of_units і виведіть знову для store.
# Додайте метод з ім’ям set_number_of_units(), що дозволяє задати кількість видів товару. 
# Викличте метод з новим числом, знову виведіть значення. Додайте метод з ім’ям 
# increment_number_of_units(), який збільшує кількість видів товару на задану величину.
# Викличте цей метод для store.

# Напишіть клас Discount(), що успадковує від класу Shop(). 
# Додайте атрибут з ім’ям discount_products для зберігання списку товарів, на які встановлена
# знижка. Напишіть метод get_discounts_ptoducts, який виводить цей список. 
# Створіть екземпляр store_discount і викличте цей метод.
# Додатково. Збережіть код класу Shop() у модулі. Створіть окремий файл, що імпортує клас 
# Shop(). Створіть екземпляр all_store і викличте один з методів Shop(), щоб перевірити, 
# що команда import працює вірно. 
# У вихідних даних наведений можливий варіант результатів виконання завдань.


class Shop():
    def __init__(self, shop_name, store_type, number_of_units = 10):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units

    def describe_shop(self):
        print(self.shop_name)
        print(self.store_type)

    def open_shop(self):
        print('The store is open.')
    
    def set_number_of_units(self, set_number_of_units):
        self.set_number_of_units = set_number_of_units

    def increment_number_of_units(self, units):
        self.number_of_units += units

store_1 = Shop('Rozetka','internet shop')
print(store_1.shop_name)
print(store_1.store_type)
store_1.describe_shop()
print(store_1.number_of_units)
store_1.open_shop()
store_1.number_of_units = 150
print(store_1.number_of_units)
store_1.increment_number_of_units(100)
print(store_1.number_of_units)

store_2 = Shop('Foxtrot', 'retail')
store_2.describe_shop()
store_2.open_shop()