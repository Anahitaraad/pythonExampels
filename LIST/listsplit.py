import random
#txt = input('enter ur names in a line followed by , then space ?').split(',')
txt = input('enter ur names in a line followed by , then space ?')
print(txt)
txt = txt.split(',')
print(txt)
y = len(txt)
print(y)
rand = random.randint(0, y)
print(rand)
print(txt[rand-1])