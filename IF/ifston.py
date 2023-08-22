import asciiart
import random
user = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n '))
print('you choose : ')
if user == 0:
    print(asciiart.rock)
elif user == 1:
    print(asciiart.paper)
else:
    print(asciiart.scissors)
com = random.randint(0, 2)
print('computer choose: ')
if com == 0:
    print(asciiart.rock)
elif com == 1:
    print(asciiart.paper)
else:
    print(asciiart.scissors)
if user == com:
    print('It is a tie!')
elif user == 0:
    if com == 2:
        print('You win!')
    else:
        print('You lose, computer win!')
elif user == 1:
    if com == 0:
        print('You win!')
    else:
        print('You lose, computer win!')
elif user ==2:
    if com == 1:
        print('You win!')
    else:
        print('You lose, computer win!')