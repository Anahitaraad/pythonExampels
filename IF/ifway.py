crossroad = input('You´re at a crossroads. Where do you want to go? Type "left" or "right“ please? ').lower()
if crossroad == 'left' :
    print('You can continue ur way.')
    print('You have come to a lake. There is an island in the middle of the lake.')
    choose = input('Type "wait" to wait for a boat or type "swim" to swim across? ').lower()
    if choose == 'wait' :
        print('You can continue ur way by boat.')
        print('''
              .,.,\______/,..,.
        ''')
        room = input('You arrive at the castle unharmed. There are 3 doors. One "red", one "yellow" and one "blue". Which color do you choose?').lower()
        if room == 'red':
            print('It is full of fire. Game Over! ')
        elif room == 'yellow':
            print('You enter a room of beasts. Game Over! ')
        elif room == 'blue':
            print('You found the treasure! You Win!')
    else:
        print('Sorry! Game over.')
else:
    print('Sorry! it is a dead-end way. Game over.')

