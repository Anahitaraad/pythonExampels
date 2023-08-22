number = 3
# global_scope

def show_number():
    number = 1
    print (number)
    return number
#local_scope

print(show_number() + 5)
print(number)


def show_number(number):
    number += 1
    print (number +1)
    return number+2

number = show_number(number)
print(number)


def calculate_num(num):
    number = num
    return number *10

print(calculate_num(number))


number = 3
def show_number():
    number = 5
    return number

print(number)
number = show_number()
print(number)

num = 3
number = 10
def show_number():
    global num
    num -= 1

print(num)
show_number()
print(num)


