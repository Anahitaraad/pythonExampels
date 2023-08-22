name = input('what is your name?')
last = input('what is your last name?')
age = input('how old are you?')
sport = input('what is your favorite sport?')
dig1 = len(name)
dig2 = len(last)
sentence = f'''Hello {name} {last}!
your first name has {dig1} characters and your last name has {dig2} characters!
you are {age} years old and your favorite sport is {sport}!'''
print(sentence)

a = input('a: ')
b = input('b: ')
exp= a
a=b
b= exp
print("a: " + a)
print("b: " + b)

print(len(input('what is your name?')))