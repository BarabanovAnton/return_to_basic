print('Вас приветствует "интеллектуальная" игра "Угадай число". Нужно угадать число от 1 до 100.')
number_player = int(input('Введите число: '))
number = 12
count = 0
while number_player != number:
    if number_player > number:
        count += 1
        print(f'Число {number_player} больше загаданного числа. Количество попыток равно {count}. Попытайтесь снова.')
        number_player = int(input('Введите число: '))
    elif number_player < number:
        count += 1
        print(f'Число {number_player} меньше загаданного числа. Количество попыток равно {count}. Попытайтесь снова.')
        number_player = int(input('Введите число: '))
else:
    count += 1
    print(f'Вы угадали число. Количество попыток {count}')