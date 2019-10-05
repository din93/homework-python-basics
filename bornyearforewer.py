bornyear_pushkin = "1799"
answer = ''

while answer!=bornyear_pushkin:
    answer = input("Напишите год рождения русского поэта А.С. Пушкина:")
    if answer==bornyear_pushkin:
        print('Верно, 1799-й год.')
    else:
        print(f'Неверно, не {answer}! Гугл в помощь, товарищ.')