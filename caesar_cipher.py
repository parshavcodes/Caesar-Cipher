from caesar_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


'''The commented code below also works but it is lengthy'''

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encrypted message is {cipher_text}")


# def decrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The decrypted message is {cipher_text}")


# if direction != "encode" or "decode":
#     print("You have entered an INVALID input")

# elif direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)

# elif direction == "decode":
#     decrypt(plain_text=text, shift_amount=shift)

'''The code below is shorter'''


def caesar(plain_text, shift_amount, direction):
    cipher_text = ""
    if direction == "decode":
        shift_amount *= -1
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            #new_letter = alphabet[new_position]
            cipher_text += alphabet[new_position]

        else:
            cipher_text += char
    print(f"The {direction}d text is {cipher_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26  # It is helpful when user enters a number which is out of index range
    caesar(plain_text=text, shift_amount=shift, direction=direction)

    result = input("Type 'yes' if you want to continue, else type 'no' .")
    if result == "no":
        should_continue = False
    print("Goodbye! ")
