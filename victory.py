from math import ceil, floor

bornyear_list = [
    ('Владимира Маяковского', '1893'),
    ('Михаила Ломоносова', '1711'),
    ('Уильяма Шекспира', '1564'),
    ('Сэра Йэна Маккелена', '1939'),
    ('Илона Маска', '1971'),
    ('Васи Петрова', '1922'),
    ('Хидео Кодзимы', '1963')
]
wanna_play = 'да'

while wanna_play.lower() == 'да':
    mistakes_count = 0
    for name, bornyear in bornyear_list:
        answer = input(f"Какой год рождения у {name}? ")
        if answer!=bornyear:
            mistakes_count += 1
    right_answers_count = len(bornyear_list)-mistakes_count
    print(f'Итак, у вас {right_answers_count} правильных ответов и {mistakes_count} неправильных ответов')
    print(f'Т.е. правильных ответов у вас {ceil(right_answers_count*100/len(bornyear_list))}%, неправильных ответов у вас соответственно {floor(mistakes_count*100/len(bornyear_list))}%')
    if mistakes_count>0:
        print('На всякий случай сообщаем, что просмотр исходного кода данной программы с целью получения ответов НИКОИМ ОБРАЗОМ НЕ ВОЗБРАНЯЕТСЯ')
    wanna_play = input("Начать сначала? (да или нет) ")
