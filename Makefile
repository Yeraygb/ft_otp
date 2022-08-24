NAME = ft_otp
FILENAME = main.py
PATH = $(cat key.hex)

rename:
	@chmod u+x $(FILENAME)
	@ln -s $(FILENAME) $(NAME)
	@echo 📄 "\033[92;3;4mft_otp created\033[0m"

clean:
	@rm -f $(NAME)
	@echo 🗑 "\033[31;3;4mft_otp delete\033[0m"

g:
	@python3 $(NAME) -g key.hex
	@echo 🔑 "\033[93;3;4mkey encripted ft_otp created\033[0m"

k:
	@python3 $(NAME) -k ft_otp.key
	@echo 🔐 "\033[93;3;4mnumber created\033[0m"

o:
	@oathtool --totp $(cat key.hex)

comprobar:
	@python3 $(NAME) -k ft_otp.key
	@oathtool --totp $(PATH)

