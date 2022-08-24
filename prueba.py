""" import cryptocode

str_encoded = cryptocode.encrypt("I am okay","wow")
print(str_encoded)
## And then to decode it:
str_decoded = cryptocode.decrypt(str_encoded, "wow")
print(str_decoded) """

from cryptography.fernet import Fernet
import sys

with open(sys.argv[1], "rb") as hex:
	original_hex = hex.read()
hex_key = int(original_hex, 16)
hex_key = str(original_hex)
key = Fernet.generate_key()
with open(".key", "wb") as a:
	a.write(key)
key = Fernet(key)
with open("ft_opt.key", "wb") as f:
	f.write(key.encrypt(hex_key.encode()))
	print("Key succesfully encrypted into ft_otp.key")

with open(".key", "rb") as filekey:
	key = filekey.read()
key = Fernet(key)
with open(sys.argv[2], "rb") as q:
	master_key = q.read()
decryted_data = key.decrypt(master_key)
print(decryted_data)
nombre = len(decryted_data) - 1
decryted_data = decryted_data[2:nombre]
print(decryted_data)






""" with open(sys.argv[1], 'r') as file:
	original_hex = file.read()
print(original_hex)
encrypted_data = encrypt(original_hex, fernet)
print(encrypted_data) """

""" encrypted_data = open(sys.argv[1], 'r')
encrypted_data = encrypted_data.read()
print("arhivo abierto:", encrypted_data)
encrypted_data = bytes(encrypted_data, encoding='utf-8')
print(encrypted_data)

decryted_data = decryted(encrypted_data, fernet)
print(decryted_data) """



""" with open(sys.argv[1], 'rb') as enc_file:
		encrypted_data = enc_file.read()
	#num_otp_key = len(encrypted_data) - 1
	#encrypted_data = encrypted_data[2:num_otp_key]
	print(encrypted_data)
	#encrypted_data = bytes(encrypted_data, encoding='utf-8')
	print(encrypted_data)
	
decryted_data = decryted(encrypted_data, fernet)
print(decryted_data) """




""" str1 = "I am okay"
key = Fernet.generate_key()
  
fernet = Fernet(key)
  
enctex = fernet.encrypt(str1.encode())
  
dectex = fernet.decrypt(enctex).decode()

print("The primordial string: ", str1)
print("The Encrypted message: ", enctex)
print("The Decrypted message: ", dectex) """