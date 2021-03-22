from random import choice
def question():
    ans = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да","Можешь быть уверен в этом", "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да, но это не точно", "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]
    return choice(ans)

name = input('Как тебя зовут? \n')
print(f' \nПривет {name}, я магический шар, и я знаю ответ на любой твой вопрос.')

flag = 'да'
while flag == 'да':
    print('Напиши вопрос на который ты хочешь узнать ответ (на который можно ответить да или нет): \n')
    user_ask = input()
    print('-', question())
    flag1 = True
    while flag1:
        flag = input('Ты хочешь задать еще вопрос? (да/нет) \n').lower()
        if flag == 'нет':
            print('Возвращайся если возникнут вопросы!')
            break
        elif flag == 'да':
            flag1 = False
        else:
            print(f'Я не понял твой ответ - {flag}, попробуй еще раз!')