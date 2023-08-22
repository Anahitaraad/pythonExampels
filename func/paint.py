import math
def painting_wall(height, width, coverage):
    print(f'number of cans = {math.ceil((height*width)/coverage)}')

painting_wall(3, 9, 5)


width = int(input('what is the width of the wall? '))
height = int(input('what is the height of the wall? '))
coverage = 5

def cans_calculator(height, width, coverage):
     number_of_cans = (height*width) /coverage
     print(f'you need {math.ceil(number_of_cans)} cans of paint')

cans_calculator(height, width, coverage)


