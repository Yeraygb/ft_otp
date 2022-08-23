""" import cryptocode

str_encoded = cryptocode.encrypt("I am okay","wow")
print(str_encoded)
## And then to decode it:
str_decoded = cryptocode.decrypt(str_encoded, "wow")
print(str_decoded)

from cryptography.fernet import Fernet
 
str1 = "I am okay"
key = Fernet.generate_key()
  
fernet = Fernet(key)
  
enctex = fernet.encrypt(str1.encode())
  
dectex = fernet.decrypt(enctex).decode()

print("The primordial string: ", str1)
print("The Encrypted message: ", enctex)
print("The Decrypted message: ", dectex) """