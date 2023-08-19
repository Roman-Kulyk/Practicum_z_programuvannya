# Визначте відсоток малих і великих літер у тексті, що зберігається у файлі. Скористайтеся, як зразком вхідного 
# текстового файла, файл The Count of Monte Cristo із сайту Project Gutenberg’s . Використайте функцію isalpha().

with open('ex_#883_9_Count_of_Monte_Cristo.txt', 'rt' ) as freading:
    lines = freading.read()


lower = ''#it initialize an empty string for lower letter
upper = ''#it initialize an empty string for upper letter   
for i in lines:#it checks every character in lines
    if i.isalpha() and i.islower():#if it alpha and lowercase
        lower += i#it adds this char to lower string
    elif i.isalpha() and i.isupper():#it it alpha and uppercase
        upper += i#it adds this char to upper string
    else:
        continue


total = (len(lines))
upper_num = (len(upper))#it assigns quantity of upper chars to variable
lower_num = (len(lower))#it assigns quantity of lower chars to variable

per_upper = upper_num/total * 100 #it counts percentage of upper chars
per_lower = lower_num/total * 100 #it counts percentage of lower chars

print(f'Percentage of lowercase letter is {per_lower:.2f}')#it prints percentage of upper chars
print(F'Percentage of uppercase letter is {per_upper:.2f}')#it prints percentage of lower chars