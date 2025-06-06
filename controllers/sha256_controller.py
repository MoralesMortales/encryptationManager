import os
from tkinter import messagebox
from models.sha256_model import SHA256Model
from views.sha256_view import SHA256View

class SHA256Controller:
    def __init__(self, root):
        self.root = root
        self.model = SHA256Model()
        self.view = SHA256View(root, self)
        self.setup_commands()
    
    def setup_commands(self):
        # Comandos pestaña Hash
        self.view.btn_generate.config(command=self.generate_hash)
        self.view.btn_verify.config(command=self.verify_hash)
        self.view.btn_clear.config(command=self.clear_all)
        
        # Comandos pestaña Archivos
        self.view.btn_browse.config(command=self.browse_file)
        self.view.btn_encrypt_file.config(command=self.encrypt_file)
        self.view.btn_decrypt_file.config(command=self.decrypt_file)
    
    # Métodos para pestaña Hash
    def generate_hash(self):
        text = self.view.get_text()
        if not text:
            self.view.show_error("No hay texto para hashear")
            return
        
        try:
            hash_result = self.model.generate_hash(text)
            self.view.set_hash(hash_result)
            self.view.update_status("Hash SHA-256 generado correctamente")
        except Exception as e:
            self.view.show_error(f"Error generando hash: {str(e)}")
    
    def verify_hash(self):
        text = self.view.get_text()
        hash_to_verify = self.view.get_hash()
        
        if not text or not hash_to_verify:
            self.view.show_error("Falta texto o hash para verificar")
            return
        
        try:
            if self.model.verify_hash(text, hash_to_verify):
                self.view.show_message("Verificación", "¡El hash coincide con el texto!")
                self.view.update_status("Verificación exitosa")
            else:
                self.view.show_message("Verificación", "El hash NO coincide con el texto")
                self.view.update_status("Verificación fallida")
        except Exception as e:
            self.view.show_error(f"Error en verificación: {str(e)}")
    
    def clear_all(self):
        self.view.clear_all()
        self.view.update_status("Campos limpiados")
    
    # Métodos para pestaña Archivos
    def browse_file(self):
        file_path = self.view.ask_file()
        if file_path:
            self.view.set_file_path(file_path)
    
    def encrypt_file(self):
        file_path = self.view.get_file_path()
        password = self.view.get_password()
        
        if not file_path or not os.path.exists(file_path):
            self.view.show_error("Seleccione un archivo válido")
            return
        
        if not password:
            self.view.show_error("Ingrese una contraseña")
            return
        
        try:
            encrypted_path = self.model.encrypt_file(file_path, password)
            self.view.show_message("Éxito", f"Archivo encriptado guardado como:\n{encrypted_path}")
            self.view.update_status(f"Archivo encriptado: {os.path.basename(encrypted_path)}")
        except Exception as e:
            self.view.show_error(f"Error encriptando archivo: {str(e)}")
    
    def decrypt_file(self):
        file_path = self.view.get_file_path()
        password = self.view.get_password()
        
        if not file_path or not os.path.exists(file_path):
            self.view.show_error("Seleccione un archivo válido")
            return
        
        if not file_path.endswith('.enc'):
            self.view.show_error("El archivo debe tener extensión .enc")
            return
        
        if not password:
            self.view.show_error("Ingrese la contraseña")
            return
        
        try:
            # Obtener la extensión original si es posible
            original_ext = None
            if '.' in os.path.basename(file_path.replace('.enc', '')):
                original_ext = '.' + file_path.split('.')[-2]
            
            decrypted_path = self.model.decrypt_file(file_path, password, original_ext)
            self.view.show_message("Éxito", f"Archivo desencriptado guardado como:\n{decrypted_path}")
            self.view.update_status(f"Archivo desencriptado: {os.path.basename(decrypted_path)}")
        except Exception as e:
            self.view.show_error(f"Error desencriptando archivo: {str(e)}")
