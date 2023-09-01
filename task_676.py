# 676. Напишіть функцію для перевірки чи є послідовність чисел геометричної 
# прогресією чи ні. Примітка. У математиці геометрична прогресія або геометрична 
# послідовність є послідовністю чисел, де кожний елемент після першого знайдений 
# шляхом множення попереднього на фіксовану, ненульову кількість, що називається 
# загальним співвідношенням. Наприклад, послідовність 2, 6, 18, 54,... є геометричною 
# прогресією з загальним співвідношенням 3. Аналогічно, 10, 5, 2.5, 1.25,... є 
# геометричною послідовністю з загальним співвідношенням 1/2.
'''
Вхідні дані:
2 6 18 54
10 5 2.5 1.25
5 8 9 11

Вихідні дані:
True
True
False
'''
def if_geometric():

    seq = [float(item) for item in input("Enter the list members: ").split(' ')]
    seq = sorted(seq)#it returns sequense in order

    if len(seq) >  1:#in case sequence larger than 1
        const = seq[1] / seq[0]#constant is equal list member 1 / list member 0
    else:
        return True
    

    for i in range(len(seq) - 1):
        if seq[i + 1] / seq[i] != const:
            return False
    return True


print(if_geometric())
