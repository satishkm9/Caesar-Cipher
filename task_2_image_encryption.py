from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, key, output_path):
    try:
        # Check if file exists
        if not os.path.isfile(image_path):
            raise FileNotFoundError(f"File not found: {image_path}")

        # Open image
        image = Image.open(image_path)
        image_array = np.array(image)
        
        # Apply XOR operation to each pixel with the key
        encrypted_array = image_array ^ key
        
        # Convert array back to image
        encrypted_image = Image.fromarray(encrypted_array)
        encrypted_image.save(output_path)
        print(f"Image encrypted and saved to {output_path}")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt_image(encrypted_image_path, key, output_path):
    try:
        # Check if file exists
        if not os.path.isfile(encrypted_image_path):
            raise FileNotFoundError(f"File not found: {encrypted_image_path}")

        # Open encrypted image
        encrypted_image = Image.open(encrypted_image_path)
        encrypted_array = np.array(encrypted_image)
        
        # Apply XOR operation to each pixel with the key (decrypts it)
        decrypted_array = encrypted_array ^ key
        
        # Convert array back to image
        decrypted_image = Image.fromarray(decrypted_array)
        decrypted_image.save(output_path)
        print(f"Image decrypted and saved to {output_path}")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print("Simple Image Encryption Tool")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            image_path = input("Enter the full path of the image to encrypt: ").strip()
            print(f"Received image path: {image_path}")  # Debugging line
            if not os.path.isfile(image_path):
                print(f"File not found: {image_path}")
                continue
            key = int(input("Enter the encryption key (0-255): "))
            output_path = input("Enter the output path for the encrypted image (with filename and extension): ").strip()
            encrypt_image(image_path, key, output_path)
        elif choice == '2':
            encrypted_image_path = input("Enter the full path of the image to decrypt: ").strip()
            print(f"Received encrypted image path: {encrypted_image_path}")  # Debugging line
            if not os.path.isfile(encrypted_image_path):
                print(f"File not found: {encrypted_image_path}")
                continue
            key = int(input("Enter the decryption key (0-255): "))
            output_path = input("Enter the output path for the decrypted image (with filename and extension): ").strip()
            decrypt_image(encrypted_image_path, key, output_path)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

#------------------------------------------------------------------------------------#
#How to use this 
#provide Full path to encrypt like: D:/Image/1.png

#Now, provide full path to save the encrypt image like:- D:/Image/ecry_image.png

#Now to decrypt follow the above steps to provide path
#--------------------------------------------------------------------------------------#
