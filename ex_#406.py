#406. Збережіть кілька понять, пов’язаних з комп’ютерами та Інтернетом, у кортежі і у списку. 
# Назвіть відповідно їх hardware (кортеж) і software (список). Виведіть усі назви по черзі. 
# Спробуйте замінити один з елементів у списку і у кортежі, і зробіть висновок щодо можливості 
# зміни елементів для цих двох типів.

software =['os','utilities','drivers']
hardware = ('keyboard','monitor','mouse','system block')

software[1] = 'pc games'
print(software)

hardware[1] = 'printer'
print(hardware)
#TypeError: 'tuple' object does not support item assignment
