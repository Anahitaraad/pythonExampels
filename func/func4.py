import math
def uppercase(word):
    print(word.upper())

uppercase('anahita')
def sum_sub_mul(a,b):
    print(f'sum is: {a + b}')
    print(f'subtraction is: {a - b}')
    print(f'multiplication is: {a * b}')

sum_sub_mul(2,3)
def maxim(a,b,c):
    numbers = [a, b, c]
    print(max(numbers))

maxim(1,9,5)
def count_Vowels(word):
    vowel = ['a','e','i','o','u']
    number_v =0
    number_c =0
    for x in word:
        if x in vowel:
            number_v += 1
        else:
            number_c += 1
    print(f'number of vowel is: {number_v}')
    print(f'number of consonant is: {number_c}')

count_Vowels('anahita')

