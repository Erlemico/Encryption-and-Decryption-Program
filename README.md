# Encryption-and-Decryption-Program
This project implements basic encryption and decryption methods, including the Shift Cipher and Substitution Cipher. It allows encrypting plaintext messages and decrypting ciphertext using a predefined key.

# Table of Contents
- Installation
- Usage
- Functions
    - shift_encrypt
    - shift_decrypt
    - substitution_encrypt
    - substitution_decrypt
- Examples
- License

# Installation
To use the program, download the script and ensure you have Python installed.
Run the functions directly within a Python environment, or import them into your project.

# Clone this repository
git clone https://github.com/username/encryption-decryption-program.git

# Usage
This program allows you to encrypt and decrypt messages using two main techniques:
Shift Cipher: Shifts each letter by a fixed number within the alphabet.
Substitution Cipher: Substitutes each letter in the plaintext with a corresponding letter from a random alphabet key.

# Functions
# shift_encrypt(text, shift)
Encrypts a message using the Shift Cipher.

- Parameters:
    - text (str): The plaintext message to encrypt.
    - shift (int): The number of positions to shift each letter.
- Returns: str - The encrypted message.

# shift_decrypt(text, shift)
Decrypts a message encrypted with the Shift Cipher.
- Parameters:
  - text (str): The encrypted message to decrypt.
  - shift (int): The shift number used during encryption.
- Returns: str - The decrypted plaintext.

# substitution_encrypt(text, key)
Encrypts a message using a Substitution Cipher with a provided key.
- Parameters:
    - text (str): The plaintext message to encrypt.
    - key (str): A 26-character string representing the substitution alphabet.
- Returns: str - The encrypted message.

# substitution_decrypt(text, key)
Decrypts a message encrypted with the Substitution Cipher.
- Parameters:
    - text (str): The encrypted message to decrypt.
    - key (str): The substitution alphabet key used for encryption.
- Returns: str - The decrypted plaintext.


# Examples

# Shift Cipher
message = "Hello World"
shift = 3
encrypted = shift_encrypt(message, shift)
print("Encrypted:", encrypted)  # Encrypted message

decrypted = shift_decrypt(encrypted, shift)
print("Decrypted:", decrypted)  # Original message

# Substitution Cipher
message = "Hello World"
key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Example key
encrypted = substitution_encrypt(message, key)
print("Encrypted:", encrypted)  # Encrypted message

decrypted = substitution_decrypt(encrypted, key)
print("Decrypted:", decrypted)  # Original message

# License
This project is licensed under the MIT License.
