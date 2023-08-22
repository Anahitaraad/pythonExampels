import random
world_list = ['sweden','apple','camel']
chosen_word = random.choice(world_list)
print(chosen_word)
#leg = len(world_list)
#print(leg)
time = 0
display = []
for x in chosen_word:
    display.append('_')
print(display)
leng = len(chosen_word)
#print(leng1)
#print("_" * leng)
#print(display)
#while time < 6:
    #guess = input('guess a letter? ').lower()
    #time += 1
    #for element in chosen_word:
        #if element == guess:
            #print('ok')
            #print(chosen_word.index(guess))
        #else:
            #print('not ok')
while display != list(chosen_word) and time < 6:
    guess = input('guess a letter: ').lower()
    time += 1
    for indexi in range(leng):
        letter = chosen_word[indexi]
        if letter == guess:
            display[indexi] = letter
    print(display)
print(display)

