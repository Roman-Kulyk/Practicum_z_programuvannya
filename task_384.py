# 384. Напишіть програму для друку літери M за допомогою введеного користувачем символа.
"""
Вхідні дані:
%

Вихідні дані:

 %   %
 %   %
 %% %%
 % % %
 %   %
 %   %
 %   %
"""
char = input("Enter your character: ")
print(char+" "*3 +char)
print(char+" "*3 +char)
print(char*2+" " +char*2)
print(char+ " " + char + " " +char)
print(char+" "*3 +char)
print(char+" "*3 +char)
print(char+" "*3 +char)