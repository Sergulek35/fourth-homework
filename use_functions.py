"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

check = 0
spent = 0
story = {}
yes = ['да', 'Да', 'ДА']
no = ['нет', 'Нет', 'НЕТ']


def separator(simbol):
    return simbol * 40


def refill_check(check):
    sum_buy = int(input('Введите сумму - '))
    check += sum_buy
    return check


while True:
    print(separator('/'))
    print(f'Ваш счёт: {check}')
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print(separator('-'))

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        check = refill_check(check)
    elif choice == '2':
        while True:
            buy = int(input('Введите сумму покупки - '))
            if check >= buy:
                buy_name = input('Введите название покупки: ')
                check -= buy
                story[buy_name] = buy
                spent += buy
                print(separator('*'))
                continued = input('Продолжить покупки? ')
                if continued in yes:
                    print(separator('.'))
                elif continued in no:
                    print('СПАСИБО ЗА ПОКУПКУ!')
                    break
                else:
                    print(separator('*'))
                    print('Неверный ввод !\nВы в главном меню!')
                    break
            else:
                print('Увы, не хватает средств на счетё!')
                print(separator(','))
                refill = input('Хотите пополнить счёт? ')
                if refill in yes:
                    check = refill_check(check)
                    print('Счёт пополнен! Продолжаем')
                    print(separator(','))
                else:
                    print(separator('*'))
                    print('Вы в главном меню!')
                    break

    elif choice == '3':
        print(separator('~'))
        print(f'Потрачено: {spent}')
        print(f'Всего покупок - {len(story)}')
        numbering = 0
        for key, value in story.items():
            numbering += 1
            print(f'{numbering}) {key} ... {value}')

    elif choice == '4':
        print(separator('^'))
        print('Вы вышли!')
        break
    else:
        print('Неверный пункт меню')
