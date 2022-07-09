"""[Программа, которая переводит цифры из Римских в Арабские]"""

Roman_numbers = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
flag = True
result = 0
print('======================----Римские цифры----======================\n')
print('Напоминание Римских цифр:')
for i in Roman_numbers:
    print(f'{i} = {Roman_numbers[i]}')

# Проверка вводимых символов
while flag:
    user_num = input('\nВведите Римское число: ')
    for i in user_num:
        if i in Roman_numbers:
            if i == user_num[-1]:
                flag = False
            else:
                continue
        else:
            print('Вы ввели не верные символы, попробуйте еще раз.')
            break       
# Перевод из Римских цифр в арабские
for i, n in enumerate(user_num):
    if len(user_num) > i + 1 and Roman_numbers[user_num[i]] < Roman_numbers[user_num[i + 1]]:
        result -= Roman_numbers[user_num[i]]
    else:
        result += Roman_numbers[user_num[i]]
print(f'\nВы ввели Римское число - {user_num} которое равно арабскому числу - {result}')
print(input('нажмите Enter для завершения программы: '))
        
