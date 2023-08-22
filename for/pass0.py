letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
import random
print("Welcome to the PyPassword Generator!")
letter = int(input('how many letters would you like in ur password? '))
number = int(input('how many numbers would you like in ur password?'))
symbol = int(input('how many letters would you like in ur password?'))
let = len(letters)
lst = []
for i in range(0, letter):
    ran = random.randint(0, let+1 )
    print(letters[ran])
    lst.append(letters[ran])
print(lst)
print(f"Your password is {''.join(lst)}")
num = len(numbers)
lst1 = []
for k in range(0, number):
    ran1 = random.randint(0, num+1 )
    print(numbers[ran1])
    lst1.append(numbers[ran1])
print(lst1)
print(f"Your password is {''.join(lst1)}")
sym = len(symbols)
lst2 = []
for j in range(0, symbol):
    ran2 = random.randint(0, sym+1 )
    print(symbols[ran2])
    lst2.append(symbols[ran2])
print(lst2)
print(f"Your password is {''.join(lst2)}")
print(lst, lst1, lst2)
lst4 = lst+lst1+lst2
print(f"Your password is {''.join(lst4)}")






