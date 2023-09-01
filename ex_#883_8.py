# Завантажте текстову версію книги The Life and Adventures of Robinson Crusoe By Daniel Defoe із сайту Project 
# Gutenberg’s . Витягніть із тексту заголовки усіх розділів, які мають вигляд, на зразок: CHAPTER I—START IN LIFE. 
# Запишіть знайдені назви у новий файл chapters.txt.


#it opens file and read it
freading = open('ex_#883_8_Robinzon_Crusoe.txt', 'rt' )

#it read the file line by line 
for line in freading:
    if "CHAPTER " in line:#and check if there is a word CHAPTER
        
        #in case there is the word it open another file
        freading = open('ex_#883_8_chapters.txt','at')
        freading.write(line)#and writes this line to the file
        freading.close()
