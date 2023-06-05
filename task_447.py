# 447. Напишіть програму, яка приймає послідовність рядків (порожній рядок для 
# завершення програми) як вхідний рядок і друкує рядки у верхньому регістрі.
'''
Вхідні дані:
python
ruby
go
 

Вихідні дані:
PYTHON
RUBY
GO
'''
txt = ""
while True:
    txt = input("Enter your string: ")
    if txt == "":
         break
    print(txt.upper())
    