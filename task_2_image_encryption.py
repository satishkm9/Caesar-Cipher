from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    """Encrypts the image by modifying pixel values based on a key."""
    image = Image.open(input_path)
    np_image = np.array(image)

    # Encrypt the image using a simple operation
    encrypted_image = (np_image + key) % 256

    # Save the encrypted image
    encrypted_image = Image.fromarray(encrypted_image.astype(np.uint8))
    encrypted_image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(input_path, output_path, key):
    """Decrypts the image by reversing the encryption operation."""
    image = Image.open(input_path)
    np_image = np.array(image)

    # Decrypt the image using the reverse operation
    decrypted_image = (np_image - key) % 256

    # Save the decrypted image
    decrypted_image = Image.fromarray(decrypted_image.astype(np.uint8))
    decrypted_image.save(output_path)
    print(f"Decrypted image saved to {output_path}")

def main():
    print("Image Encryption and Decryption Tool")
    choice = input("Would you like to (E)ncrypt or (D)ecrypt an image? ").upper()

    if choice not in ['E', 'D']:
        print("Invalid choice! Please choose either 'E' for encryption or 'D' for decryption.")
        return

    input_path = input("Enter the input image path: ")
    output_path = input("Enter the output image path: ")
    try:
        key = int(input("Enter the encryption/decryption key (an integer): "))
    except ValueError:
        print("Invalid key! Please enter an integer.")
        return

    if choice == 'E':
        encrypt_image(input_path, output_path, key)
    else:
        decrypt_image(input_path, output_path, key)

if __name__ == "__main__":
    main()
