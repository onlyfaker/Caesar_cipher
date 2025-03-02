# Caesar Cipher

## Description
This Caesar Cipher program is a simple text encryption and decryption tool that uses the ASCII value of characters to shift them by a specified number. It features a command-line interface that guides users through the encryption and decryption process.

## Features
- Encrypt text messages by shifting ASCII values
- Decrypt encoded messages using the original shift value
- Preserves spaces in the text (spaces remain unshifted)
- User-friendly command-line interface
- Input validation to prevent errors
- ASCII art logo for visual appeal

## Requirements
- Python 3.x
- Caesar_art.py file (containing the ASCII art logo)

## Installation
1. Save the code as `caesar_cipher.py`
2. Create a file named `Caesar_art.py` with the LOGO variable
3. Run the program with Python 3: `python caesar_cipher.py`

## Usage
1. When you run the program, you'll see the Caesar Cipher logo
2. Choose an operation:
   - Type `encode` to encrypt a message
   - Type `decode` to decrypt a message
3. Enter your message
4. Specify the shift number (how many positions to shift each character)
5. View the result
6. Choose whether to continue or exit

## Example
```
Type 'encode' to encrypt, type 'decode' to decrypt: encode
Type your message: hello world
Type the shift number: 5
mjqqt|twqi

Type 'yes' if you want to go again. Otherwise type 'no': 
yes

Type 'encode' to encrypt, type 'decode' to decrypt: decode
Type your message: mjqqt|twqi
Type the shift number: 5
hello world
```

## How It Works
The program works by converting each character to its ASCII value, then either adding (for encryption) or subtracting (for decryption) the specified shift number. Spaces are preserved to maintain readability. The modified ASCII values are then converted back to characters.

## File Structure
- `caesar_cipher.py`: The main program file
- `Caesar_art.py`: Contains the ASCII art logo displayed at startup

## Note
This is a basic implementation of the Caesar Cipher. It works with all ASCII characters but is not meant for serious security purposes as the Caesar Cipher is easily breakable.
