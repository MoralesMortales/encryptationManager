from views.rsa_view import RSAView
from models.rsa_model import RSAModel
import tkinter as tk
from tkinter import messagebox, filedialog
import os

class RSAController:
    def __init__(self, root):
        self.root = root
        self.model = RSAModel()
        self.view = RSAView(root, self)
        self.setup_commands()
        self.model.generate_keys()
        self.view.update_status("Claves RSA generadas")
    
    def setup_commands(self):
        self.view.btn_generate.config(command=self.generate_keys)
        self.view.btn_save_public.config(command=self.save_public_key)
        self.view.btn_save_private.config(command=self.save_private_key)
        self.view.btn_load_public.config(command=self.load_public_key)
        self.view.btn_load_private.config(command=self.load_private_key)
        self.view.btn_encrypt.config(command=self.encrypt_text)
        self.view.btn_decrypt.config(command=self.decrypt_text)
        self.view.btn_save_encrypted.config(command=self.save_encrypted_text)
    
    def generate_keys(self):
        try:
            if self.model.generate_keys():
                self.view.update_status("Nuevas claves RSA generadas")
        except Exception as e:
            messagebox.showerror("Error", f"Error generando claves: {str(e)}")
    
    def save_public_key(self):
        try:
            # Usamos asksaveasfilename directamente sin crear nuevas ventanas
            filename = filedialog.asksaveasfilename(
                defaultextension=".pem",
                filetypes=[("Archivos PEM", "*.pem")],
                title="Guardar clave pública",
                initialfile="public_key.pem",
                parent=self.root  # Especificamos la ventana padre
            )
            if filename:
                saved_file = self.model.save_public_key(filename)
                self.view.update_status(f"Clave pública guardada en {os.path.basename(saved_file)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error guardando clave pública: {str(e)}")
    
    def save_private_key(self):
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".pem",
                filetypes=[("Archivos PEM", "*.pem")],
                title="Guardar clave privada",
                initialfile="private_key.pem",
                parent=self.root  # Especificamos la ventana padre
            )
            if filename:
                saved_file = self.model.save_private_key(filename)
                self.view.update_status(f"Clave privada guardada en {os.path.basename(saved_file)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error guardando clave privada: {str(e)}")
    
    def load_public_key(self):
        try:
            filename = filedialog.askopenfilename(
                filetypes=[("Archivos PEM", "*.pem")],
                title="Seleccionar clave pública",
                parent=self.root  # Especificamos la ventana padre
            )
            if filename:
                if self.model.load_public_key(filename):
                    self.view.update_status(f"Clave pública cargada desde {os.path.basename(filename)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error cargando clave pública: {str(e)}")
    
    def load_private_key(self):
        try:
            filename = filedialog.askopenfilename(
                filetypes=[("Archivos PEM", "*.pem")],
                title="Seleccionar clave privada",
                parent=self.root  # Especificamos la ventana padre
            )
            if filename:
                if self.model.load_private_key(filename):
                    self.view.update_status(f"Clave privada cargada desde {os.path.basename(filename)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error cargando clave privada: {str(e)}")
    
    def encrypt_text(self):
        plaintext = self.view.get_plaintext()
        if not plaintext:
            messagebox.showerror("Error", "No hay texto para encriptar", parent=self.root)
            return
        
        try:
            encrypted = self.model.encrypt(plaintext)
            self.view.set_encrypted_text(encrypted)
            self.view.update_status("Texto encriptado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error encriptando: {str(e)}", parent=self.root)
    
    def decrypt_text(self):
        encrypted = self.view.get_encrypted_text()
        if not encrypted:
            messagebox.showerror("Error", "No hay texto para desencriptar", parent=self.root)
            return
        
        try:
            decrypted = self.model.decrypt(encrypted)
            self.view.set_decrypted_text(decrypted)
            self.view.update_status("Texto desencriptado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error desencriptando: {str(e)}", parent=self.root)
    
    def save_encrypted_text(self):
        encrypted = self.view.get_encrypted_text()
        if not encrypted:
            messagebox.showerror("Error", "No hay texto encriptado para guardar", parent=self.root)
            return
        
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".enc",
                filetypes=[("Archivos encriptados", "*.enc")],
                title="Guardar texto encriptado",
                parent=self.root  # Especificamos la ventana padre
            )
            if filename:
                with open(filename, "w") as f:
                    f.write(encrypted)
                self.view.update_status(f"Texto encriptado guardado en {os.path.basename(filename)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error guardando archivo: {str(e)}", parent=self.root)
