"""Древняя китайская игра в палочки.

Играют два игрока.  Есть n палочек. Игроки по очереди берут от одной до трёх палочек. 
Играют до тех пор пока не закончатся палочки. Тот кто взял последним - тот проиграл."""
print('\n===================----Древняя Китайская игра в палочки----=================== \n')
user_1 = input('Введите имя первого игрока \n')
user_2 = input('Введите имя второго игрока \n')
sticks = int(input('Введите колличество палочек минимум 10 \n'))

flag = True
user = user_1
while flag:
    print(f'Играет игрок: {user}')
    
    out = int(input(f'Сколько палочек достать из {sticks} \n'))
    while out > 3 and out >= 1:
        print('Введите кол-во палочек от 1 до 3, пожалуйста')
        out = int(input(f'Сколько палочек достать из {sticks} \n'))
    sticks -= out
    if sticks > 0:
        # Смена игроков 
        if user == user_1:
            user = user_2
        elif user == user_2:
            user = user_1
    else:
        print(f'Игрок: {user} проиграл ^_^')
        print(input('Для выхода нажмите Enter: '))
        flag = False