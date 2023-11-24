# 589.Комп’ютерний вірус атакував файлову систему суперкомп’ютера і пошкодив контроль прав 
# доступу до файлів. Для кожного файлу є відомий набір операцій, які можуть бути застосовані до 
# нього: писати (W), читати (R), виконати (X). Перший рядок містить число n - кількість файлів, 
# що містяться у файловій системі. Наступні n рядків містять імена файлів і дозволені операції 
# з ними, розділені пропусками. Наступний рядок містить ціле число m - кількість операцій з 
# файлами. В наступних m рядках записані операції, які виконуються над файлами. До одного файлу 
# можна звертатися багато разів. Для кожного запиту програма повинна надрукувати OK, якщо 
# запитана операція з файлом є можливою, або Access denied, якщо операцію виконати неможливо.
"""
4
helloworld.py R X
pinglog W R
scripts R
goodluck X W R
5

  
write helloworld.py
execute scripts
read pinglog
write pinglog

Вихідні дані:
OK
Access denied
Access denied
OK
OK
"""
def process_operations(file_permissions, operations):
    for operation in operations:
        file, op = operation.split()
        if file in file_permissions and op in file_permissions[file]:
            print("OK")
        else:
            print("Access denied")

n = int(input("Enter amount of files: "))#it asks about amoutn of files
file_permissions = {}#it initializes an empty dictionary

for _ in range(n):#it asks to inpute file name and permissions related to it
    file, *permissions = input("Enter your files and permissions: ").split()

    file_permissions[file] = set(permissions)#it adds new key, value pair to dictionary

m = int(input("Enter amount of requests: "))#it asks about amoutn of requests
operations = [input("Enter your requests: ") for _ in range(m)]#it inputs request itself

process_operations(file_permissions, operations)#it calls the function
