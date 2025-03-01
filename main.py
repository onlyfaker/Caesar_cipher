
def encode(msg1,shift_num1):
    ascii_values = [ord(char) for char in msg1]
    length_for_iteration = len(ascii_values)
    for vall in range(length_for_iteration):
        ascii_values[vall] += shift_num1
    characters = [chr(value) for value in ascii_values]
    print(''.join(characters))

def decode(msg2,shift_num2):
    ascii_values = [ord(char) for char in msg2]
    length_for_iteration = len(ascii_values)
    for vall in range(length_for_iteration):
        ascii_values[vall] -= shift_num2
    characters = [chr(value) for value in ascii_values]
    print(''.join(characters))

#todo - make it so that it doesnt count spaces in ascii
again='yes'
while(again=='yes'):
    user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if user_input=='encode':
        msg1 = input('Type your message: ')
        shift_num1=int(input('Type the shift number: '))
        encode(msg1,shift_num1)

    if user_input=='decode':
        msg2 = input('Type your message: ')
        shift_num2=int(input('Type the shift number: '))
        decode(msg2,shift_num2)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.")



