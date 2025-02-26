# def text_to_ascii(text):
#     ascii_values = []
#     for char in text:
#         ascii_values.append(ord(char))
#     return ascii_values
#todo-make encode/decode function take the message(its letters) and move the letters by the shift number, so like
#so figure out a way to seperate those letters and use their ascii value with shifter to encode/decode...


user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")

def encode(msg1,shift_num1):
    pass

def decode(msg2,shift_num2):
    pass
#todo - add availabilty to go again if you answerd yes, use while loop...

if user_input=='encode':
    msg1 = input('Type your message: ')
    shift_num1=int(input('Type the shift number: '))
    # ascii_numbers_input = text_to_ascii(msg1)
    encode(msg1,shift_num1)

if user_input=='decode':
    msg2 = input('Type your message: ')
    shift_num2=int(input('Type the shift number: '))
    decode(msg2,shift_num2)


