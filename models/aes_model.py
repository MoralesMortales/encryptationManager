from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

class AESModel:
    def __init__(self):
        self.key = get_random_bytes(32)  # Clave AES de 256 bits
        self.iv = None
    
    def generate_key(self):
        self.key = get_random_bytes(32)
    
    def get_key_b64(self):
        return base64.b64encode(self.key).decode('utf-8')
    
    def encrypt(self, plaintext):
        self.iv = get_random_bytes(16)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        datos = plaintext.encode('utf-8')
        datos_encriptados = cipher.encrypt(pad(datos, AES.block_size))
        return base64.b64encode(self.iv + datos_encriptados).decode('utf-8')
    
    def decrypt(self, encrypted_text):
        resultado = base64.b64decode(encrypted_text.encode('utf-8'))
        iv = resultado[:16]
        datos_encriptados = resultado[16:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(datos_encriptados), AES.block_size).decode('utf-8')
