#156. Напишіть програму, щоб визначити, чи задане ціле число (вводиться користувачем) парне або непарне.

num = int(input("Enter a numbre: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")