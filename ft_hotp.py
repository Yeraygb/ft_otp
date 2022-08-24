import hmac, base64, struct, hashlib, time
from cryptography.fernet import Fernet



def get_hotp_token(secret, intervals_no):
	key = base64.b16decode(secret, True)
	#decodificar la key
	msg = struct.pack(">Q", intervals_no)
	#conversiones entre valores de Python y estructuras C representadas
	h = hmac.new(key, msg, hashlib.sha1).digest()
	o = o = h[19] & 15
	#genera un hash usando ambos. El algoritmo hash es HMAC
	h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
	#unpacking
	return h

def get_totp_token(decryted):
	#asegurarse de dar el mismo otp durante 30 segundos
	x = str(get_hotp_token(decryted, intervals_no=int(time.time())//30))

	while len(x)!=6:
		x+='0'
	return x

#base64 encoded key
""" with open('ft_otp.key', 'rb') as enc_file:
	encrypted = enc_file.read()
secret = base64.b64encode(encrypted).decode("latin-1")
print(get_totp_token(secret)) """