# Зчитайте зі стандартного вводу цілі числа, по одному числу у рядку, і після 
# першого введеного нуля виведіть суму отриманих на вхід чисел.
num_list = []
num = 1
while num != 0:
    num = int(input("Enter your number: "))
    num_list.append(num)
    # break
print(sum(num_list))