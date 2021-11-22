"""
При помощи вложенных циклов (можно while, можно for) и оператора IF нарисовать фигуры представленные ниже.
Пользователь вводит, с клавиатуры, высоту фигуры в символах.

  D         *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
  * * * * * * * * * * *
* * * * * * * * * * * * *
  *         *         *
    *       *       *
      *     *     *
        *   *   *
          * * *
            *

"""

height = int(input("Введите число(высота ромба): "))
height_diamond = height // 2 - 1
# СОЗДАЕМ ПИРАМИДУ
for i in range(2 * height_diamond + 1):
    if i <= height_diamond:
        print('  ' * (height_diamond - i) + ' *' * (i + 1) + ' *' * i)
    else:
        if i == (height_diamond * 2):              # СОЗДАЕМ НИЗ И ЛИНИЮ
            print('  ' * height_diamond + ' *')
        else:
            print('  ' * (i - height_diamond) + ' *', end='')
            print('  ' * (2 * height_diamond - i - 1) + ' *' + '  ' * (2 * height_diamond - i - 1) + ' *')