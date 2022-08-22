#------------------------------ LIBRERIAS ------------------------------------xw
 
import argparse
import sys
 
key_file_name = "ft_otp.key"
 
# ----------------------------- CONFIGURACION --------------------------------
 
def is_hex(key_hex):
	"""Function to verify if string is hex of 64 characters"""
	if len(key_hex) >= 64:
		try:
			int(key_hex, 16)
		except ValueError:
			return False
		return True
	else:
		return False
 
def save_key(key_hex):
   """Function to save the key ciphered"""
   pass
 
def args_conf():
	parser = argparse.ArgumentParser(
		description = 'Time One-Time Password implementation.'
	)
	# Save ciphered ft_otp.key
	parser.add_argument('-g', '--new-key', help = 'Save hexadecimal key in ft_otp.key', default = None)
	# Generate new key
	parser.add_argument('-k', '--key-gen', help = 'Generate new totp autentication code', default = None, action = 'store_true')
 
	args = parser.parse_args()
	return args
 
"""Este programa recibe una clave hexadecimal de al menos 64 caracteres como argumento,
guarda esa clave cifrada en un archivo ft_otp.key y genera una contraseña temporal"""
 
# -------------------------------- EJECUCION ----------------------------------
 
def main():
	args = args_conf()
	if args.new_key:
		with open(sys.argv[2], 'rt') as file:
			original_hex = file.read()
		if is_hex(original_hex) is False:
			print("Error, you must set an hexadecimal password of 64 characters or more")
		else:
			save_key(original_hex)
			print("Key succesfully encrypted into ft_otp.key")
 
if __name__ == "__main__":
   main()
