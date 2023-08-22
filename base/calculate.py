def summa(n1, n2):
    return n1 + n2

def minnus(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    #doc.string
    '''returs the division '''
    return n1 / n2


operations = {
    '+': add,
    '-': minnus,
    '*': multiplication,
    '/': division

}

def calculator():
    game_on = True

    while game_on:

        go_again = input("Type 'y' to continue, or type 'n' to start from the scratch, or type 'exit ").lower()
        if go_again == "exit":
            game_on = False
        elif  go_again == "y":
            operations()
























