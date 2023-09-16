import art
def caesar(text, shift_to_move, cipher_direction):
    message=""
    if(direction=="encode"):
        for char in text:
            if char in alphabet:
                position=alphabet.index(char)
                new_position=position+shift_to_move
                new_letter=alphabet[new_position]
            #encrypted_message+=alphabet[(alphabet.index(text[i])+shift_to_move)]
                message+=new_letter
            else:
                message+=char
    elif(direction=="decode"):
        for char in text:
            if char in alphabet:
                position=alphabet.index(char)
                new_position=position-shift_to_move
                new_letter=alphabet[new_position]
                message+=new_letter
            else:
                message+=char
            
    print(f"The {cipher_direction} text is {message}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ,'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)
execute=True
while execute:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text_input = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift>26:
        shift%=26
    caesar(text=text_input, shift_to_move=shift, cipher_direction=direction)
    answer=input("Would you like to encode/decode again? Type yes or no: ").lower()
    if(answer=="no"):
        execute=False
    
