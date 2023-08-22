alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def ceaser(text, shift, direction):
    new_text = ''
    if direction == 'encode':
        #shift_new *= -1
        #baray inke 2ta fun 1ja tarif beshan, mitoonim in karo konim.
        for letter in text:
            position = alphabet.index(letter)
            new_index = position + shift #(_new)
            new_text += (alphabet[new_index])
        print(new_text)
        #print(f' here is ur {direction}d result: {new_text} )

    elif direction == 'decode':
        for letter in text:
            position = alphabet.index(letter)
            new_index = position - shift
            new_text += (alphabet[new_index])
        print(new_text)
    else:
        print('wrong')


ceaser(text, shift, direction)













