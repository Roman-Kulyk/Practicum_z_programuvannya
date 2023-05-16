# 337. Виведіть усі символи ASCII з кодами від n (n > 32) до m (m < 127) 
# і їх коди в наступному вигляді: «символ код».
'''
Вхідні дані:
101
106
Вихідні дані:
e 101
f 102
g 103
h 104
i 105
j 106
'''

n = int(input("Enter a first symbol: "))
m = int(input("Enter a last symbol: "))
for i in range(n,m+1):
    print(chr(i),i)#Returns the string representing a character whose Unicode code point is the integer i.