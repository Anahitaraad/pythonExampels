name = input('enter your name: ')
if len(name) >= 5:
    print('ok')
else:
    print('not')

number = int(input('Which number do you want to check? '))
if (number) % 2 == 0:
        print('This is an even number.')
else:
        print('This is an odd number.')