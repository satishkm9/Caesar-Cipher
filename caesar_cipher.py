def caesar_cipher_encrypt(text, shift):
    """Encrypts the text using Caesar Cipher with the given shift."""
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    """Decrypts the text using Caesar Cipher with the given shift."""
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption and Decryption")
    choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? ").upper()

    if choice not in ['E', 'D']:
        print("Invalid choice! Please choose either 'E' for encryption or 'D' for decryption.")
        return

    text = input("Enter the message: ")
    try:
        shift = int(input("Enter the shift value: "))
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
    main()
