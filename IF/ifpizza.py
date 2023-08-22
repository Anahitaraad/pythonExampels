print('Welcome to Python Pizza Deliveries !')
size = input('What size pizza do you want? S, M, or L ? ')
peperoni = input('do u want peperoni? Y or N ? ')
cheese = input('do u want cheese? Y or N ? ')
total = 0
if size == 's':
    total += 15
elif size == 'm':
    total += 20
else:
    total += 25

if peperoni == 'y':
    if size == 'y':
        total += 2
    else:
        total += 3

if cheese == 'Y':
    total += 1

print(f'you should pay {total}.')

bill = float(input('what was the total bill?'))
tip = float(input('how much tip would you like to give? '))
people = int(input('how many people to split the bill? '))
amount = (bill/people) * (1 + tip/100)
print(f'each person should pay: {round(amount, 2)}')