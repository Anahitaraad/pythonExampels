import random
from hangmanart import stages
world_list = ['sweden', 'apple', 'camel']
chosen_word = random.choice(world_list)
print(chosen_word)
lives = 6
display = []
game = True
for x in chosen_word:
    display.append('_')
print(display)
leng = len(chosen_word)
while game:
    guess = input('guess a letter: ').lower()
    for indexi in range(leng):
        letter = chosen_word[indexi]
        if letter == guess:
            display[indexi] = letter
            print(display)
    if guess not in chosen_word:
        lives -= 1
    print(f'{stages[lives]}\n you loose a life')
    if '_' not in display:
        game = False
        print('you win')
    elif lives == 0:
       game = False
       print('GAME OVER')
    print(f"{''.join(display)}")





print(display)
