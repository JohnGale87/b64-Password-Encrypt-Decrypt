import base64


def encrypt_pass(password):
    encoded_bytes = base64.b64encode(password.encode())
    print(encoded_bytes)


def decode_pass(password):
    decode_bytes = base64.b64decode(password)
    decode_data = decode_bytes.decode()
    print(f"decoded password: {decode_data}")

print("""
1.Password Encryption
2.Decrypt a password that has been encrypted using this program""")
select = int(input("What service do you require: "))

if select == 1:
    user_password = input("Enter your password: ")
    encrypt_pass(user_password)
else:
    encode_string = input ("Enter the b64 string: ")
    decode_pass(encode_string)
