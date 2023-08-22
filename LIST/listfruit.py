fruits = ['strawberry','blueberry','apple','grape','peach','cherry','pear']
fruits[-1] = 'melon'
fruits.append('lemon')
print(fruits)
vegetables = ['spinach', 'kale', 'tomato','celery','potato']
foods = [fruits, vegetables]
print(foods)
print(foods[1][1])

veg = ['tomato', 'cucumber']
fruit = ['banana', 'apple']
food = [veg, fruit]
print(food)
foods = veg + fruit
print(foods)

fruits = ['apple','orange','banana', True, 13, 13.8]
#f = 'it is not'
#print(f)

for fruit in fruits:
    #print(type(fruit))
    #fruits.append('loop')
    print(fruit)
    print(f'{fruit} Pie')
    print(fruits)

#print(fruit)
print(fruits)