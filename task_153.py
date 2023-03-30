#153. Визначити чверть координатної площини, якій належить точка A з координатами (x1, y1). 
#Відомо, що координати не рівні нулю і є цілими числами.

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

if x > 0:
    if y > 0:
        print("I")
    elif y < 0:
        print("IV")
elif x < 0:
    if y > 0:
        print("II")
    elif y < 0:
        print("III")
else:
    pass