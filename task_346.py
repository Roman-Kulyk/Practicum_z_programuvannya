# 346. Напишіть програму, щоб отримати рядок із введеного користувачем рядка, 
# де всі входження першого символа у рядку змінилися на рядок *HIDE*, 
# за винятком першого.
'''
Вхідні дані:
Endless clouds drifted back and forth, blotting out the RED SUN
Вихідні дані:
Endl*HIDE*ss clouds drift*HIDE*d back and forth, blotting out th*HIDE* R*HIDE*D SUN
'''
txt = input("Enter a string: ")

frag_1 = txt[:1]
frag_2 = txt[1:]
a = txt[0]
print(a)
#b = a.lower()
#print(b)
print(frag_1.upper()+frag_2.replace(frag_1,"*HIDE*"))

