#------------------------------- LIBRERIAS ------------------------------------

import tkinter as tk
from tkinter import ttk
from turtle import width
from cryptography.fernet import Fernet
import ft_hotp
import qrcode
from otp import encrypt

""" def encrypt(hex_key):
	key = Fernet.generate_key()
	with open(".key", "wb") as a:
		a.write(key)
	key = Fernet(key)
	with open("ft_otp.key", "wb") as f:
		f.write(key.encrypt(hex_key.encode()))
	print("Key succesfully encrypted into ft_otp.key") """

def i_g(file1):
	with open(file1, 'rb') as file:
		original_hex = file.read()
	hex_key = int(original_hex, 16)
	hex_key = str(original_hex)
	otp.encrypt(hex_key)

def i_k(file):
	with open(".key", "rb") as filekey:
			key1 = filekey.read()
	key = Fernet(key1)
	with open(file, 'rb') as q:
		encrypted_data = q.read()
	decryted_data = key.decrypt(encrypted_data)
	c = len(decryted_data) - 1
	decryted_data = decryted_data[2:c]
	print(ft_hotp.get_totp_token(decryted_data))
	code = ft_hotp.get_totp_token(decryted_data)
	with open("code.txt", "wt") as e:
		e.write(code)

def i_q():
	with open("code.txt", "rt") as z:
		code = z.read()
	data = code
	filename = "qrcode.png"
	img = qrcode.make(data)
	img.save(filename)

def interactive():
	# Create a window
	frame = tk.Tk()
	frame.title("interactive otp")

	frame.geometry('400x200+500+500')

	# Buttons
	button1 = ttk.Button(frame, text="-g save hexadecimal key", command=lambda: i_g("key.hex"))
	button1.pack()

	button2 = ttk.Button(frame, text="-k generate new totp", command=lambda: i_k("ft_otp.key"))
	button2.pack()

	button3 = ttk.Button(frame, text="-q generate a qr", command=lambda: i_q())
	button3.pack()

	button4 = ttk.Button(frame, text='Exit', command=lambda: frame.quit())
	button4.pack()

	frame.mainloop()