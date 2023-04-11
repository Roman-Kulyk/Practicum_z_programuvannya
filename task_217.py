#217. Надрукувати всі цілі числа від a до b включно, кратні деякому числу c. 
# Числа a, b, c - цілі числа, які вводить користувач.

a,b,c = input("Enter three number through the spacebar: ").split(" ")
for i in range(int(a),int(b) + 1):
    if i %  int(c) == 0:
        print(i, end = " ")
print()