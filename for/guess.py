import random
world_list = ['sweden','apple','camel']
chosen_word = random.choice(world_list)
print(chosen_word)
leng = len(chosen_word)
display = []
for x in chosen_word:
    display.append('_')
#for _ in range(leng):
    #display += '_'
print(display)
#while '_' in display:
    #guess = input('guess aletter:').lower()

while not display == list(chosen_word):
    guess = input('guess a letter: ').lower()
    for indexi in range(leng):
        letter = chosen_word[indexi]
        if letter == guess:
            display[indexi] = letter
    print(display)

print(display)



