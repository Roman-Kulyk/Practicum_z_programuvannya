#205. Напишіть програму-таймер зворотного відліку, яка запитує у користувача кількість секунд n, 
# з якої слід починати відлік.


n = int(input("Enter a number of second: "))

for i in range(n,0,-1):
    print(i)
print("Start!")
