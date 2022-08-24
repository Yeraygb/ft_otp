#------------------------------- LIBRERIAS ------------------------------------

import argparse
from cgi import print_environ
import sys
from cryptography.fernet import Fernet
import ft_hotp

# ------------------------------ ENCRIPTAR ----------------------------------

def encrypt(hex_key):
	key = Fernet.generate_key()
	with open(".key", "wb") as a:
		a.write(key)
	key = Fernet(key)
	with open("ft_otp.key", "wb") as f:
		f.write(key.encrypt(hex_key.encode()))
	print("Key succesfully encrypted into ft_otp.key")

# -------------------------------- EJECUCION ----------------------------------

def args_conf():
	parser = argparse.ArgumentParser(
		description = 'Time One-Time Password implementation.'
	)
	# Save ciphered ft_otp.key
	parser.add_argument('-g', '--new-key', help = 'Save hexadecimal key in ft_otp.key', default = None)
	# Generate new key
	parser.add_argument('-k', '--key-gen', help = 'Generate new totp autentication code', default = None)

	args = parser.parse_args()
	return args

def main():
	args = args_conf()
	if args.new_key:
		with open(sys.argv[2], 'rb') as file:
			original_hex = file.read()
		hex_key = int(original_hex, 16)
		hex_key = str(original_hex)
		encrypt(hex_key)
	elif args.key_gen:
		with open(".key", "rb") as filekey:
			key1 = filekey.read()
		key = Fernet(key1)
		with open(sys.argv[2], 'rb') as q:
			encrypted_data = q.read()
		decryted_data = key.decrypt(encrypted_data)
		c = len(decryted_data) - 1
		decryted_data = decryted_data[2:c]
		print(ft_hotp.get_totp_token(decryted_data))

if __name__ == "__main__":
	main()
