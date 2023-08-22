# 1-function with output and a string parameter
# 2_ input as an argument
# 3- inside the function:

def str_length(str):
    count = 0
    for char in str:
        count +=1
    return count


strng = input('enter anything? ')
print(str_length(strng))