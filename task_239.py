# 239. Намалювати сходинки як у вихідних даних, використовуючи символи пропуску і решітки #, 
# коли на вхід програми подається ціле число n - кількість сходинок.


n = int(input("Enter a number: "))
for n in range(1, n+1):
    print('#'*n)

