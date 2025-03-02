from Caesar_art import LOGO

def encode(msg1,shift_num1):
    ascii_values = []
    for vall in msg1:
        if vall == ' ':  # If the character is a space
            ascii_values.append(ord(vall))  # Add space without shifting
        else:
            ascii_values.append(ord(vall) + shift_num1)  # Shift non-space characters
    characters = [chr(value) for value in ascii_values]
    print(''.join(characters))

def decode(msg2,shift_num2):
    ascii_values = []
    for char in msg2:
        if char == ' ':  #If the character is a space
            ascii_values.append(ord(char))  # Add space without shifting
        else:
            ascii_values.append(ord(char) - shift_num2)  # Shift non-space characters
    characters = [chr(value) for value in ascii_values]
    print(''.join(characters))

print(LOGO)
again='yes'
while(again=='yes'):
    # Get and validate user operation choice
    while True:
        user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
        if user_input == 'encode' or user_input == 'decode':
            break
        else:
            print("Invalid input. Please type 'encode' or 'decode'!!!\n")

    # Process based on validated choice
    if user_input == 'encode':
        msg1 = input('Type your message: ')
        shift_num1 = int(input('Type the shift number: '))
        encode(msg1, shift_num1)

    else:  # user_input must be 'decode' here
        msg2 = input('Type your message: ')
        shift_num2 = int(input('Type the shift number: '))
        decode(msg2, shift_num2)

    # Get and validate user's choice to continue
    while True:
        again = input("\nType 'yes' if you want to go again. Otherwise type 'no': \n").lower()
        if again == 'yes' or again == 'no':
            break
        else:
            print("Invalid input. Please type 'yes' or 'no': ")
print('hi')



