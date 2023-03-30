#141. Перевести число, введене користувачем, у байти або кілобайти в залежності від його вибору. 
#Користувач вводить значення у мегабайтах і, відповідно, вводить напрямок переведення: 
#B (у байти) або KB (у кілобайти).

number = int(input('Enter a number of Mb: '))
option = str(input('Enter an option to transfer: '))

if option == "B":
    print(number * 1024 * 1024)
elif option == "kB":
    print(number * 1024)
