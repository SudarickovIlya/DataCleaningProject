try:
    print('Начало программы')
    a = input('Введите число: ')
    b = int(a)
except ValueError as e:
    print(e)
    print('Нечисловое выражение')
else:
    print('Все в порядке')
finally:
    print('Закончено')