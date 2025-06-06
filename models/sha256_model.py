import hashlib
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

class SHA256Model:
    def __init__(self):
        self.hash_object = None
    
    def generate_hash(self, text):
        """Genera el hash SHA-256 del texto proporcionado"""
        self.hash_object = hashlib.sha256(text.encode())
        return self.hash_object.hexdigest()
    
    def verify_hash(self, text, hash_to_verify):
        """Verifica si el texto coincide con el hash proporcionado"""
        new_hash = hashlib.sha256(text.encode()).hexdigest()
        return new_hash == hash_to_verify
    
    def encrypt_file(self, file_path, password):
        """Encripta un archivo usando una contraseña (convertida a SHA-256 como key)"""
        try:
            # Generar clave de 32 bytes (256 bits) del hash SHA-256 de la contraseña
            key = hashlib.sha256(password.encode()).digest()
            
            # Leer contenido del archivo
            with open(file_path, 'rb') as f:
                file_data = f.read()
            
            # Generar IV y cifrar
            iv = get_random_bytes(16)
            cipher = AES.new(key, AES.MODE_CBC, iv)
            encrypted_data = cipher.encrypt(pad(file_data, AES.block_size))
            
            # Guardar archivo encriptado (.enc)
            encrypted_file_path = file_path + '.enc'
            with open(encrypted_file_path, 'wb') as f:
                f.write(iv + encrypted_data)
            
            return encrypted_file_path
        except Exception as e:
            raise Exception(f"Error encriptando archivo: {str(e)}")
    
    def decrypt_file(self, encrypted_file_path, password, original_extension=None):
        """Desencripta un archivo usando una contraseña"""
        try:
            # Generar clave de 32 bytes (256 bits) del hash SHA-256 de la contraseña
            key = hashlib.sha256(password.encode()).digest()
            
            # Leer archivo encriptado
            with open(encrypted_file_path, 'rb') as f:
                file_data = f.read()
            
            # Extraer IV y datos encriptados
            iv = file_data[:16]
            encrypted_data = file_data[16:]
            
            # Descifrar
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
            
            # Guardar archivo desencriptado
            if original_extension:
                output_path = encrypted_file_path.replace('.enc', original_extension)
            else:
                output_path = encrypted_file_path.replace('.enc', '')
            
            with open(output_path, 'wb') as f:
                f.write(decrypted_data)
            
            return output_path
        except Exception as e:
            raise Exception(f"Error desencriptando archivo: {str(e)}")
