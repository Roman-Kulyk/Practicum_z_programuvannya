# Завантажте текстову версію однієї з книг із сайту Project Gutenberg’s . Замініть усі розриви рядків у 
# тексті символом пропуску і запишіть відформатований текст у новий файл formatted_text.txt.

with open('ex_#883_7_Tom_Sawyer.txt', 'rt' ) as freading:
    lines = freading.read()

txt = lines.replace(" ", "·")
#print(txt)

freading = open('ex_#883_7_formatted_text.txt','wt')
freading.write(txt)
freading.close()