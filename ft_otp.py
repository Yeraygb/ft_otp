#!/usr/bin/python3

#------------------------------- LIBRERIAS ------------------------------------

import argparse
from cgi import print_environ
from curses import window
import sys
from cryptography.fernet import Fernet
import ft_hotp
import qrcode
import inter

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
	# Generate code
	parser.add_argument('-k', '--key-gen', help = 'Generate new totp autentication code', default = None)
	# Generate qr
	parser.add_argument('-q', '--qr-gen', help = 'Generate qr with totp code', default = None)
	# Interactive
	parser.add_argument('-i', '--inter', help = 'Run the program interactively', action = 'store_true')

	args = parser.parse_args()
	return args

def g():
	with open(sys.argv[2], 'rb') as file:
		original_hex = file.read()
	hex_key = int(original_hex, 16)
	hex_key = str(original_hex)
	encrypt(hex_key)

def k():
	with open(".key", "rb") as filekey:
			key1 = filekey.read()
	key = Fernet(key1)
	with open(sys.argv[2], 'rb') as q:
		encrypted_data = q.read()
	decryted_data = key.decrypt(encrypted_data)
	c = len(decryted_data) - 1
	decryted_data = decryted_data[2:c]
	print(ft_hotp.get_totp_token(decryted_data))
	code = ft_hotp.get_totp_token(decryted_data)
	with open("code.txt", "wt") as e:
		e.write(code)

def q():
	with open("code.txt", "rt") as z:
		code = z.read()
	data = code
	filename = "qrcode.png"
	img = qrcode.make(data)
	img.save(filename)


def main():
	args = args_conf()
	if args.new_key:
		g()
	elif args.key_gen:
		k()
	elif args.qr_gen:
		q()
	elif args.inter:
		inter.interactive()


if __name__ == "__main__":
	main()
