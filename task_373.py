# 373. Вводиться рядок. Необхідно визначити в ньому відсотки малих і великих букв.
'''
Вхідні дані:
Hello, Guido!

Вихідні дані:
61.54
15.38
'''
string = input("Enter string:") #it takes a string from user
count1 = 0 #it initialize variable for lowercase letter
count2 = 0 #it initialize variable for uppercase letter
for i in string: #it checks every item in a strin and
      if(i.islower()): #if it is lower
            count1 = count1 + 1 #increase the amount of lowercase letter
      elif(i.isupper()): #if it is upper
            count2 = count2 + 1 #increase the amount of uppercase letter

length = len(string)
perc_1 = count1/length * 100
perc_2 = count2/length * 100

print(f"Percentage of lower is {perc_1:.2f}")
print(f"Percentage of upper is {perc_2:.2f}")




