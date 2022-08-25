OTP

DEFINITION:

	The ft_otp program allows you to register an initial key, and is capable of generating a new password every x seconds.

	•With the -g option, the program must receive as an argument a hexadecimal key of at least 64 characters. The program safely stores this key in a file called ft_otp.key, which will be encrypted at all times.

	•With the -k option, the program generates a new temporary password and prints it to standard output

BONUS:

	The bonus make a qr with the new temporary password and make a interactive windows.

	•With the -q option, the program must create qr

	•With the -i option, the program generates a intereactive window

REQUIREMENTS:

	pip install qrcode
	pip install tk
	pip install Pillow
	pip install cryptography

	pip install setuptools, to check if the program works correctly with the command: oathtool --totp $(cat key.hex), but this take a longs time

USAGE:

	$ ./ft_otp -g key.hex
	Key was successfully saved in ft_otp.key.
	$ ./ft_otp -k ft_otp.key
	836492
	$ sleep 60
	$ ./ft_otp -k ft_otp.key
	123518
	$ oathtool --totp $(cat key.hex)			<- With this command it is verified that the authenticate is correct, if it gives the same value
	123518

	The program have makefie if you wanna use:
	First of all: make rename
	make g to run -g option
	make k to run -k option
	make q to run -q option
	make i to run -i option