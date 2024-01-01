# 588. Напишіть програму, яка виводить число в стилі LCD-калькулятора. На вхід програми 
# подається послідовність цифр, яку потрібно вивести на екран в спеціальному стилі. Розмір 
# всіх цифр 4 символу в ширину і 7 символів у висоту. Між цифрами повинен бути один порожній 
# стовпець. Перед першою цифрою не повинно бути пропусків. Виведені цифри повинні бути обведені 
# рамочкою, в кутах якої знаходиться символ x, горизонтальна лінія створюється з символу -, 
# а вертикальна - з символу вертикальної риски |. Користувач вводить рядок - послідовність цифр, 
# а програма має вивести 9 рядків, що містять цифри, записані в зазначеному форматі.
"""
Вхідні дані:
0123456789
123
4

Вихідні дані:
x--------------------------------------------------x
| --        --   --        --   --   --   --   --  |
||  |    |    |    | |  | |    |       | |  | |  | |
||  |    |    |    | |  | |    |       | |  | |  | |
|           --   --   --   --   --        --   --  |
||  |    | |       |    |    | |  |    | |  |    | |
||  |    | |       |    |    | |  |    | |  |    | |
| --        --   --        --   --        --   --  |
x--------------------------------------------------x
x---------------x
|      --   --  |
|   |    |    | |
|   |    |    | |
|      --   --  |
|   | |       | |
|   | |       | |
|      --   --  |
x---------------x
x-----x
|     |
||  | |
||  | |
| --  |
|   | |
|   | |
|     |
x-----x
"""
