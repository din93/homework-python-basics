bornyear_pushkin = "1799"
bornday_pushkin = "26 мая"

answer_bornyear = input("Напишите год рождения русского поэта А.С. Пушкина: ")
if answer_bornyear==bornyear_pushkin:
    print('Верно, 1799-й год.')
    answer_bornday = input("А день его рождения? ")
    if answer_bornday==bornday_pushkin:
        print('Верно, 26 мая. Ты вообще молодец!')
    else:
        print(f'Нет, не {answer_bornday}! Загляника в поисковик еще раз.')
else:
    print(f'Неверно, не {answer_bornyear}! Гугл в помощь, товарищ.')