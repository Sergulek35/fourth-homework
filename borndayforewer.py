"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""





def user_year_day(year_day, d_y='год'):
    question =  input(f'Введите {d_y} рождения Пушкина А.С: ')
    while question != year_day:
        print("Не верно")
        question = input(f'Введите {d_y} рождения Пушкина А.С: ')

user_year_day('1799')
user_year_day('6', 'день')
print('Верно')
