#Encryption and Decryption Program

#Encryption Program

#Shift Chiper
def shift_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            shifted = chr(((ord(char) - 65 + shift) % 26) + 65)
            encrypted_text += shifted if is_upper else shifted.lower()
        else:
            encrypted_text += char
    return encrypted_text

#Substitution Chiper

#Random Alphabet
def substitution_encrypt_random_alphabet(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_message = ''

    for char in message:
        if char.lower() in alphabet:
            is_upper = char.isupper()
            char_index = alphabet.index(char.lower())
            encrypted_char = key[char_index]
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_message += encrypted_char
        else:
            encrypted_message += char

    return encrypted_message

#Rotate by (ROT)
def substitution_encrypt_rot(message, key):
    encrypted_message = ''
    
    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            offset = ord('A') if is_upper else ord('a')
            encrypted_char = chr((ord(char) - offset + key) % 26 + offset)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
            
    return encrypted_message

#Vigenere Chiper
def vigenere_encrypt(message, key):
    encrypted_message = ''
    
    key = key.upper()
    key_index = 0
    
    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            offset = ord('A') if is_upper else ord('a')
            key_char = key[key_index % len(key)]
            key_offset = ord(key_char)
            encrypted_char = chr((ord(char) - offset + key_offset - offset) % 26 + offset)
            encrypted_message += encrypted_char
            key_index += 1
        else:
            encrypted_message += char
            
    return encrypted_message

#Affine Chiper
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_encrypt(message, key_a, key_b):
    encrypted_message = ''
    
    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            offset = ord('A') if is_upper else ord('a')
            encrypted_char = chr(((ord(char) - offset) * key_a + key_b) % 26 + offset)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
            
    return encrypted_message

#Hill Chiper
import numpy as np

def hill_cipher_encrypt(plain_text, key_matrix):
    plain_text = plain_text.replace(" ", "").lower()
    key_matrix = np.array(key_matrix)
    
    block_size = len(key_matrix)
    padding = block_size - len(plain_text) % block_size
    if padding != block_size:
        plain_text += "X" * padding
    
    encrypted_text = ""
    for i in range(0, len(plain_text), block_size):
        block = [ord(char) - ord('A') for char in plain_text[i:i+block_size]]
        block = np.array(block)
        
        encrypted_block = np.dot(key_matrix, block) % 26
        encrypted_block = [chr(char + ord('A')) for char in encrypted_block]
        
        encrypted_text += ''.join(encrypted_block)
    
    return encrypted_text

#Transposition Chiper

#Simple Columnar Approach
def simple_columnar_transposition_encrypt(message, key):
    # Menghapus spasi dari pesan dan mengubahnya menjadi huruf kapital
    message = message.replace(" ", "")
    key = key.upper()
    
    # Menghitung jumlah kolom berdasarkan panjang kunci
    num_columns = len(key)
    
    # Membuat matriks untuk penyimpanan pesan yang diubah
    encrypted_matrix = [[''] * num_columns for _ in range((len(message) // num_columns) + 1)]
    
    # Mengisi matriks dengan karakter dari pesan
    col = 0
    row = 0
    for char in message:
        encrypted_matrix[row][col] = char
        col += 1
        if col == num_columns:
            col = 0
            row += 1
    
    # Mengurutkan kolom matriks berdasarkan urutan karakter dalam kunci
    sorted_columns = [list(row) for row in zip(*encrypted_matrix)]
    sorted_columns = [list(column) for _, column in sorted(zip(key, sorted_columns))]
    
    # Menggabungkan kolom menjadi teks terenkripsi
    encrypted_text = ''
    for row in sorted_columns:
        encrypted_text += ''.join(row)
    
    return encrypted_text

#Keyword Columnar Approach
def keyword_columnar_transposition_encrypt(message, keyword):
    message = message.replace(" ", "")
    keyword = keyword.upper()
    
    # Membangun kunci yang unik dari keyword
    unique_chars = []
    for char in keyword:
        if char not in unique_chars:
            unique_chars.append(char)
    keyword_key = ''.join(unique_chars)
    
    # Menghitung jumlah kolom berdasarkan panjang kunci
    num_columns = len(keyword_key)
    
    # Membuat matriks untuk penyimpanan pesan yang diubah
    encrypted_matrix = [[''] * num_columns for _ in range((len(message) // num_columns) + 1)]
    
    # Mengisi matriks dengan karakter dari pesan
    col = 0
    row = 0
    for char in message:
        encrypted_matrix[row][col] = char
        col += 1
        if col == num_columns:
            col = 0
            row += 1
    
    # Mengurutkan kolom matriks berdasarkan urutan karakter dalam kunci
    sorted_columns = [list(row) for row in zip(*encrypted_matrix)]
    sorted_columns = [list(column) for _, column in sorted(zip(keyword_key, sorted_columns))]
    
    # Menggabungkan kolom menjadi teks terenkripsi
    encrypted_text = ''
    for row in sorted_columns:
        encrypted_text += ''.join(row)
    
    return encrypted_text


#Decryption Program

#Shift Chiper
def shift_decrypt(cipher_text, shift):
    decrypted_text = ""
    for char in cipher_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            shifted = chr(((ord(char) - 65 - shift) % 26) + 65)
            decrypted_text += shifted if is_upper else shifted.lower()
        else:
            decrypted_text += char
    return decrypted_text

#Substitution Chiper

#Random Alphabet
def substitution_decrypt_random_alphabet(encrypted_message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_message = ''

    for char in encrypted_message:
        if char.lower() in key:
            is_upper = char.isupper()
            char_index = key.index(char.lower())
            decrypted_char = alphabet[char_index]
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_message += decrypted_char
        else:
            decrypted_message += char

    return decrypted_message

#Rotate by (ROT)
def substitution_decrypt_rot(encrypted_message, key):
    return substitution_encrypt_rot(encrypted_message, -key)

#Vigenere Chiper
def vigenere_decrypt(encrypted_message, key):
    decrypted_message = ''
    
    key = key.upper()
    key_index = 0
    
    for char in encrypted_message:
        if char.isalpha():
            is_upper = char.isupper()
            offset = ord('A') if is_upper else ord('a')
            key_char = key[key_index % len(key)]
            key_offset = ord(key_char)
            decrypted_char = chr((ord(char) - offset - key_offset + offset) % 26 + offset)
            decrypted_message += decrypted_char
            key_index += 1
        else:
            decrypted_message += char
            
    return decrypted_message

#Affine Chiper
def affine_decrypt(encrypted_message, key_a, key_b):
    decrypted_message = ''
    
    mod_inverse_a = mod_inverse(key_a, 26)
    if mod_inverse_a is None:
        return "Multiplicative inverse of key 'a' does not exist."

    for char in encrypted_message:
        if char.isalpha():
            is_upper = char.isupper()
            offset = ord('A') if is_upper else ord('a')
            decrypted_char = chr(((ord(char) - offset - key_b) * mod_inverse_a) % 26 + offset)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
            
    return decrypted_message

#Hill Chiper


#Transposition Chiper

#Simple Columnar Approach


#Keyword Columnar Approach



#Input and Output Encryption and Decryption Program

while True:
  print("## Welcome to Encryption and Decryption Program! ##")
  print("===================================================")
  print()

  print("Choose the Action!")
  print()

  print("1. Enter the Program")
  print("2. Close the Program")
  print()

  choice1 = int(input("Choose the Action : "))
  print()

  if choice1 == 1:
    print("Choose the Program!")
    print()

    print("1. Encryption Program")
    print("2. Decryption Program")
    print()

    choice2 = int(input("Choose the Program : "))
    print()

    if choice2 == 1:
      print("The Method of Encryption Program")
      print()

      print("1. Shift Chiper")
      print("2. Substitution Chiper")
      print("3. Vigenere Chiper")
      print("4. Affine Chiper")
      print("5. Hill Chiper")
      print("6. Transposition Chiper")
      print()

      choice3 = int(input("Choose the Method : "))
      print()

      if choice3 == 1:
        print("Shift Chiper")
        plain_text = input("Enter text to encrypted : ")
        shift_amount = int(input("Enter the key : "))
        encrypted_text = shift_encrypt(plain_text, shift_amount)
        print()
        
        print("Encrypted text : ", encrypted_text)
        print()

      elif choice3 == 2:
        print("Technique of Substitution Chiper")
        print()

        print("1. Random Alphabet")
        print("2. Rotate by (ROT)")
        print()

        choice5 = int(input("Choose the Approach : "))
        print()

        if choice5 == 1:
          print("Random Alphabet")
          user_key = input("Enter the substitution cipher key (26 unique letters) : ").lower()

          if len(user_key) != 26 or len(set(user_key)) != 26:
            print("Invalid key length or duplicate letters. Please enter a valid key.")
          else:
            message = input("Enter the message to encrypt : ")
            encrypted_message = substitution_encrypt_random_alphabet(message, user_key)
            print("Encrypted Message : ", encrypted_message)
            print()
            
        elif choice5 == 2:
          print("Rotate by (ROT)")
          key = int(input("Enter the rotation key : "))
          message = input("Enter the message to encrypt : ")

          encrypted_message = substitution_encrypt_rot(message, key)
          print("Encrypted Message :", encrypted_message)
          print()

      elif choice3 == 3:
        print("Vigenere Chiper")

        text = input("Enter text to encrypted : ")
        key = input("Enter the Key : ")

        encrypted_text = vigenere_encrypt(text, key)
        print("Encrypted Text : ", encrypted_text)
        print()

      elif choice3 == 4:
        print("Affine Chiper")
        
        key_a = int(input("Enter the multiplicative key (must be coprime with 26) : "))
        key_b = int(input("Enter the additive key : "))
        message = input("Enter the message to encrypt : ")

        encrypted_message = affine_encrypt(message, key_a, key_b)
        print("Encrypted Message : ", encrypted_message)
        print()

      elif choice3 == 5:
        print("Hill Chiper")
        plain_text = input("Enter text to encrypt : ").upper()
        key_matrix = []
        num = int(input("Enter M : "))
        for i in range(num):
          row = []
          for j in range(num):
            val = int(input(f"Enter the number of M ({i+1},{j+1}): "))
            row.append(val)
          key_matrix.append(row)

          encrypted_text = hill_cipher_encrypt(plain_text, key_matrix)
          print("Encrypted text : ", encrypted_text)
          print()

      elif choice3 == 6:
        print("Approach of Transposition Chiper")
        print()

        print("1. Simple Columnar")
        print("2. Keyword Columnar")
        print()

        choice6 = int(input("Choose the Approach : "))
        print()

        if choice6 == 1:
          print("Simple Columnar Approach")
          text = input("Enter text to encrypt : ")
          key = input("Enter the key : ")
          encrypted_text = simple_columnar_transposition_encrypt(text, key)
          print("Encrypted text : ", encrypted_text)
          print()
        elif choice6 == 2:
          print("Keyword Columnar Approach")
          text = input("Enter text to encrypt : ")
          key = input("Enter the key : ")
          encrypted_text = keyword_columnar_transposition_encrypt(text, key)
          print("Encrypted text : ", encrypted_text)
          print()

    elif choice2 == 2:
      print("The Method of Decryption Program")
      print()

      print("1. Shift Chiper")
      print("2. Substitution Chiper")
      print("3. Vigenere Chiper")
      print("4. Affine Chiper")
      #print("5. Hill Chiper")
      #print("6. Transposition Chiper")
      print()

      choice4 = int(input("Choose the Method : "))
      print()

      if choice4 == 1:
        print("Shift Chiper")
        cipher_text = input("Enter text to decrypted : ")
        shift_amount = int(input("Enter the ey : "))
        decrypted_text = shift_decrypt(cipher_text, shift_amount)
        print()

        print("Decrypted text : ", decrypted_text)
        print()

      elif choice4 == 2:
        print("Technique of Substitution Chiper")
        print()

        print("1. Random Alphabet")
        print("2. Rotate by (ROT)")
        print()

        choice6 = int(input("Choose the Approach : "))
        print()

        if choice6 == 1:
          print("Simple Columnar Approach")
          user_key = input("Enter the substitution cipher key (26 unique letters): ").lower()

          if len(user_key) != 26 or len(set(user_key)) != 26:
            print("Invalid key length or duplicate letters. Please enter a valid key.")
          else:
            message = input("Enter the message to encrypt : ")
            decrypted_message = substitution_decrypt_random_alphabet(encrypted_message, user_key)
            print("Decrypted Message : ", decrypted_message)
          
        elif choice6 == 2:
          print("Rotate by (ROT)")
          key = int(input("Enter the rotation key : "))
          message = input("Enter the message to decrypt : ")

          decrypted_message = substitution_decrypt_rot(encrypted_message, key)
          print("Decrypted Message : ", decrypted_message)
          print()

      elif choice4 == 3:
        print("Vigenere Chiper")

        key = input("Enter the encryption key : ")
        message = input("Enter the message to encrypt : ")

        decrypted_message = vigenere_decrypt(encrypted_message, key)
        print("Decrypted Message : ", decrypted_message)
        print()

      elif choice4 == 4:
        print("Affine Chiper")

        key_a = int(input("Enter the multiplicative key (must be coprime with 26) : "))
        key_b = int(input("Enter the additive key : "))
        message = input("Enter the message to encrypt : ")

        decrypted_message = affine_decrypt(encrypted_message, key_a, key_b)
        print("Decrypted Message : ", decrypted_message)
        print()

      #elif choice4 == 5:
        #print("Hill Chiper")
        #text = input("Enter text to decrypted : ")
        #print("Decrypted Text : ")
        #print()

      #elif choice4 == 6:
        #print("Approach of Transposition Chiper")
        #print()

        #print("1. Simple Columnar")
        #print("2. Keyword Columnar")
        #print()

        #choice8 = int(input("Choose the Approach : "))
        #print()

        #if choice8 == 1:
          #print("Simple Columnar Approach")
          #encrypted_message = input("Masukkan pesan terenkripsi (Simple Columnar) : ")
          #key = input("Masukkan kunci : ")
          #decrypted_message = (encrypted_message, key)
          #print("Pesan terdekripsi (Simple Columnar) : ", decrypted_message)
          #print()
          
        #elif choice8 == 2:
          #print("Keyword Columnar Approach")
          #text = input("Enter text to decrypted : ")
          #key = input("Input the Key : ")
          #decrypted_text = (text, key)
          #print("Decrypted text : ", decrypted_text)
          #print()

  elif choice1 == 2:
    print("Thanks for Using the Program")
    break

  else:
    print("Invalid Input. Try Again!")