import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
letter = int(input('how many letters would you like in ur password?\n '))
number = int(input('how many numbers would you like in ur password?\n'))
symbol = int(input('how many letters would you like in ur password?\n'))
lst = []
for i in range(0, letter):
    ran = random.randint(0, len(letters)+1 )
    lst.append(letters[ran])
print(f"Your password is {''.join(lst)}")
lst1 = []
for k in range(0, number):
    ran1 = random.randint(0, len(numbers)+1 )
    lst1.append(numbers[ran1])
print(f"Your password is {''.join(lst1)}")
lst2 = []
for j in range(0, symbol):
    ran2 = random.randint(0, len(symbols)+1 )
    lst2.append(symbols[ran2])
print(f"Your password is {''.join(lst2)}")
lst4 = lst+lst1+lst2
print(f"Your password is {''.join(lst4)}")






