NAME = ft_otp
FILENAME = ft_otp.py
PATH = $(cat key.hex)

rename:
	@chmod u+x $(FILENAME)
	@ln -s $(FILENAME) $(NAME)
	@echo 📄 "\033[92;3;4mft_otp created\033[0m"

clean:
	@rm -f $(NAME)
	@echo 🗑 "\033[31;3;4mft_otp delete\033[0m"

fclean:
	@rm -f $(NAME)
	@rm -f code.txt
	@rm -f ft_otp.key
	@rm -f .key
	@rm -f qrcode.png

g:
	@python3 $(NAME) -g key.hex
	@echo 🔑 "\033[93;3;4mkey encripted ft_otp created\033[0m"

k:
	@python3 $(NAME) -k ft_otp.key
	@echo 🔐 "\033[93;3;4mnumber created\033[0m"

q:
	@python3 $(NAME) -q code.txt
	@echo 📄 "\033[93;3;4qr created\033[0m"

i:
	@python3 $(NAME) -i


