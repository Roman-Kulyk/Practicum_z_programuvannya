#142. Визначте назву геометричної фігури за введеною кількістю її сторін. 
#Програма повинна підтримувати фігури від 3 до 6 сторін. Якщо введена кількість сторін поза межами цього діапазону, 
#програма повинна відображати відповідне повідомлення.


number = int(input('Enter a sides number: '))
if number == 3:
    print("That's a triangle.")
elif number == 4:
    print("That's a quadrilateral.")
elif number == 5:
    print("That's a pentagon.")
elif number == 6:
    print("That's a hexagon")
else:
    print("That number of sides is not supported by this program.")