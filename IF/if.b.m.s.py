#time = int(input('enter minutes: '))
#second = time * 60
#print(f'seconds are: {second}')

#kilometer = int(input('enter kilometers: '))
#mile = round(kilometer * (1/1.609344))
#print(f'it is {mile} mile')

weight = float(input('enter your weight in kilogram: '))
height = float(input('enter your height in meter: '))
bodymass = round(weight/(height * height),2)
print(f'your BMI is: {bodymass}')
if bodymass <= 18.5:
    print('u are underweight.')
elif bodymass <= 25:
    print('u are normal')
elif bodymass <= 30:
    print('u are slightly overweight.')
elif bodymass <= 35:
    print('u are obese')
else:
    print('u are clinically obese.')