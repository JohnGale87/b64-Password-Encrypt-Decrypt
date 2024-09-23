#!/usr/bin/env python3

import base64


def xor_encrypt_decrypt(input_string: str, key: int) -> str:
    # XOR each character with the key
    return "".join(chr(ord(char) ^ key) for char in input_string)


def encrypt_string(clear_text: str, key: int) -> str:
    # Encrypt the string using XOR
    encrypted_string = xor_encrypt_decrypt(clear_text, key)
    # Encode the encrypted string using base64
    encoded_bytes = base64.b64encode(encrypted_string.encode("utf-8"))
    cypher_text = encoded_bytes.decode("utf-8")
    return cypher_text


def decrypt_string(cypher_text: str, key: int) -> str:
    # Decode the base64 encoded string
    decoded_bytes = base64.b64decode(cypher_text.encode("utf-8"))
    decoded_string = decoded_bytes.decode("utf-8")
    # Decrypt the string using XOR
    clear_text = xor_encrypt_decrypt(decoded_string, key)
    return clear_text


crpytography_key = int(input("Enter your encryption key (integer):"))

print(
    "1.Password Encryption\n2.Decrypt a password that has been previously encrypted using this program"
)
select = int(input("What service do you require:"))

if select == 1:
    clear_text = input("Enter your password:")
    print(f"encrypted password: {encrypt_string(clear_text, crpytography_key)}")
elif select == 2:
    cypher_text = input("Enter the previously encrypted string:")
    print(f"decrypted password: {decrypt_string(cypher_text, crpytography_key)}")
else:
    print("Service not offered, please retry.")
