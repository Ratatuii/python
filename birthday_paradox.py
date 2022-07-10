import datetime
import random

MONTHS = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')


def getBirthdays(numberOfBirthdays):
    """ Возвращаем список объектов дат для случайных дней рождения."""
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(1995, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """Возвращаем объект даты дня рождения, встречающегося несколько раз в списке дней рождения"""
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA

# Отображаем вводную информацию
print('''Парадокс дней рождений показывает что в группе из Н человек 
совпадение дней рождений очень велико. Эта программа выполняет симуляцию Монте Карло
(Повторяющаяся генерация дней рождения) ''')
print()

# Запрашиваем верные данные у пользователя
while True:
    print('Группу из скольки человек генерировать?')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
print()
print('Первая сгенерированная группа людей имеют дни рождения:')
# Генерируем и отображаем дни рождения
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    print(f'{birthday.day} {monthName}', end='')
print()
print()

# Выясняем, встречаются ли два совпадающих дня рождения
match = getMatch(birthdays)

# Отображаем результаты
if match is not None:
    monthName = MONTHS[match.month - 1]
    print(f'Несколько человек имеют одинаковые дни рождения - {monthName} {match.day}')
else:
    print('Дни рождения не совпали')
print()
print(f'Генерируем группу из {numBDays} человек 100,000 раз...')
print()
input('Нажмите Enter для начала...')

simMatch = 0 # Число повторяющихся дней рождений в симуляции

# Производим 100 000 операций имитационного моделирования:
for i in range(100_000):
    # Сообщаем о ходе выполнения каждые 10 000 операций
    if i % 10_000 == 0:
        print(f'{i} симуляций выполнено...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) is not None:
        simMatch += 1
print('100,000 симуляций выполнено.')

# Отображаем результаты симуляции.
probability = round(simMatch / 100_000 * 100, 2)
print(f'В 100,000 симуляций из {numBDays} человек, ')
print(f'было {simMatch} совпадений дней рождений.')
print(f'Таким образом, в группе из {numBDays} человек, шанс того что совпадут дни рождения - {probability} %.')
