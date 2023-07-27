# Визначте назву геометричної фігури за введеною кількістю її сторін. 
# Програма повинна підтримувати фігури від 3 до 6 сторін. 
# Якщо введена кількість сторін поза межами цього діапазону, програма повинна 
# відображати відповідне повідомлення.


def what_is_figure(qty):
    if qty == 3:
        print("triangle")
    elif qty == 4:
        print('square')
    elif qty == 5:
        print('penthagon')
    elif qty == 6:
        print('hexagon')
    else:
        print("I don't know such a figure!")


what_is_figure(2)
what_is_figure(3)
what_is_figure(6)
what_is_figure(7)