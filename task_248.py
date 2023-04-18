# 248. Користувач вводить n-цифрове ціле число. Необхідно вивести числа, утворені із введеного, 
# відкиданням останньої цифри з кожного попереднього числа.


numbers = input("Enter a number: ")
#num_list = []
lenght = len(numbers)
for n in range(lenght,0,-1):
    print(numbers)
    list_numbers = list(numbers)
    list_numbers.pop()

    #num_list.append(n)
    print(list_numbers)