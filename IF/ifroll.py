height = int(input('how tall are u? '))
total = 0
if height >= 120:
    print('u can ride')
    age = int(input('how old are u?'))
    if age <= 12:
        print('u should pat 50')
        total = 50
    elif age <= 18:
        print('u should pay 70')
        total = 70
    elif age >= 45 and age <= 55:
        print('u can go free')
    else:
        print(' u should pay 90')
        total = 90
    photo = input('Do u want a photo? Yes or No').lower()
    if photo == 'yes':
        total +=25
    print(f'ur total bill is {total}')

else:
    print('sorry u can´t ride')