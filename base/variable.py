#a = input('a: ')
#b = input('b: ')
#c = 0
#c = a
#a = b
#b = c
#print('a = ' + a)
#print('b = ' + b)

#print('welcome to this program. ')
#city = input('which cty did u grow up? ')
#pet = input('what is ur pet name? ')
#print(f'{city}{pet} is ur band name' )
#print('ur band name is ' + city + '' + pet)

print('wlcm to the calculate.')
total = float(input('how much was the bill totally? '))
ppl = int(input('how many ppl were there? '))
tip = int(input('which percentage of tip do u want to pay? 10, 12, 15 ? '))
tip_pay = total * (tip/100)
final = round((total + tip_pay) / ppl, 1 )
print(f'each person should pay {final} €')

print('hello'[0])
