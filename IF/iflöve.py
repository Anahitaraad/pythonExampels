name1 = input('what is ur name?').lower()
name2 = input('what is ur partner´s name ?').lower()

name = name1+name2
t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')
true_total = t+r+u+e
l = name.count('l')
o = name.count('o')
v = name.count('v')
e = name.count('e')
love_total = l+o+v+e
total = int(str(true_total) + str(love_total))
if total < 10 or total > 90:
    print(f'ur score is {total}. u go together like coke and mentos.')
elif total >= 40 and total <= 50:
    print(f'ur score is {total}. u r alright together.')
else:
    print(f'ur score is {total}.')