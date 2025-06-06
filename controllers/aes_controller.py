from views.aes_view import AESView
from models.aes_model import AESModel
import tkinter as tk
from tkinter import messagebox, filedialog
import base64

class AESController:
    def __init__(self, root):
        self.root = root
        self.model = AESModel()
        self.view = AESView(root, self)
        self.setup_commands()
        self.view.update_key_display(self.model.get_key_b64())
    
    def setup_commands(self):
        self.view.btn_generate.config(command=self.generate_key)
        self.view.btn_save_key.config(command=self.save_key)
        self.view.btn_encrypt.config(command=self.encrypt_text)
        self.view.btn_decrypt.config(command=self.decrypt_text)
    
    def generate_key(self):
        self.model.generate_key()
        self.view.update_key_display(self.model.get_key_b64())
        self.view.update_status("Nueva clave AES generada")
    
    def save_key(self):
        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".key",
                filetypes=[("Archivos de clave", "*.key"), ("Todos los archivos", "*.*")],
                title="Guardar clave AES"
            )
            
            if file_path:
                with open(file_path, "w") as f:
                    f.write(self.model.get_key_b64())
                self.view.update_status(f"Clave guardada en {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar la clave: {str(e)}")
    
    def encrypt_text(self):
        plaintext = self.view.get_plaintext()
        if not plaintext:
            messagebox.showerror("Error", "No hay texto para encriptar")
            return
        
        try:
            encrypted_text = self.model.encrypt(plaintext)
            self.view.set_encrypted_text(encrypted_text)
            self.view.update_status("Texto encriptado correctamente con AES")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo encriptar el texto: {str(e)}")
    
    def decrypt_text(self):
        encrypted_text = self.view.get_encrypted_text()
        if not encrypted_text:
            messagebox.showerror("Error", "No hay texto para desencriptar")
            return
        
        try:
            decrypted_text = self.model.decrypt(encrypted_text)
            self.view.set_decrypted_text(decrypted_text)
            self.view.update_status("Texto desencriptado correctamente con AES")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo desencriptar el texto: {str(e)}")
