def caesar_cipher_encrypt(text, shift):
    """Encrypts the text using Caesar Cipher with the given shift."""
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            # Determine the ASCII base for lowercase or uppercase letters
            shift_base = ord('A') if char.isupper() else ord('a')
            # Shift character within the bounds of a-z or A-Z
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetic characters are not changed

    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    """Decrypts the text using Caesar Cipher with the given shift."""
    # Decrypting is the same as encrypting with the negative shift
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption and Decryption")
    choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? ").upper()
    print(f"Debug: User chose {choice}")

    if choice not in ['E', 'D']:
        print("Invalid choice! Please choose either 'E' for encryption or 'D' for decryption.")
        return

    text = input("Enter the message: ")
    print(f"Debug: User entered message: {text}")
    try:
        shift = int(input("Enter the shift value: "))
        print(f"Debug: User entered shift value: {shift}")
    except ValueError:
        print("Invalid shift value! Please enter an integer.")
        return

    if choice == 'E':
        encrypted_text = caesar_cipher_encrypt(text, shift)
        print(f"Encrypted message: {encrypted_text}")
    else:
        decrypted_text = caesar_cipher_decrypt(text, shift)
        print(f"Decrypted message: {decrypted_text}")

if __name__ == "__main__":
    print("Debug: Calling main function")
    main()
