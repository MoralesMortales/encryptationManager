import tkinter as tk
from tkinter import ttk

class RSAView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.create_widgets()
    
    def create_widgets(self):
        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack()
        
        # Key Management
        self.key_frame = tk.LabelFrame(self.main_frame, text="Gestión de Claves", padx=10, pady=10)
        self.key_frame.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="ew")
        
        self.btn_generate = tk.Button(self.key_frame, text="Generar Claves")
        self.btn_generate.pack(side=tk.LEFT, padx=5)
        
        self.btn_save_public = tk.Button(self.key_frame, text="Guardar Pública")
        self.btn_save_public.pack(side=tk.LEFT, padx=5)
        
        self.btn_save_private = tk.Button(self.key_frame, text="Guardar Privada")
        self.btn_save_private.pack(side=tk.LEFT, padx=5)
        
        self.btn_load_public = tk.Button(self.key_frame, text="Cargar Pública")
        self.btn_load_public.pack(side=tk.LEFT, padx=5)
        
        self.btn_load_private = tk.Button(self.key_frame, text="Cargar Privada")
        self.btn_load_private.pack(side=tk.LEFT, padx=5)
        
        # Encryption Area
        self.encrypt_frame = tk.LabelFrame(self.main_frame, text="Encriptar", padx=10, pady=10)
        self.encrypt_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 5))
        
        self.text_to_encrypt = tk.Text(self.encrypt_frame, height=10, width=40)
        self.text_to_encrypt.pack()
        
        self.btn_encrypt = tk.Button(self.encrypt_frame, text="Encriptar")
        self.btn_encrypt.pack(pady=(10, 0))
        
        # Decryption Area
        self.decrypt_frame = tk.LabelFrame(self.main_frame, text="Desencriptar", padx=10, pady=10)
        self.decrypt_frame.grid(row=1, column=1, sticky="nsew", padx=(5, 0))
        
        self.text_to_decrypt = tk.Text(self.decrypt_frame, height=10, width=40)
        self.text_to_decrypt.pack()
        
        self.btn_decrypt = tk.Button(self.decrypt_frame, text="Desencriptar")
        self.btn_decrypt.pack(pady=(10, 0))
        
        # Save Encrypted Button
        self.btn_save_encrypted = tk.Button(self.decrypt_frame, text="Guardar Encriptado")
        self.btn_save_encrypted.pack(pady=(5, 0))
        
        # Status Bar
        self.status_var = tk.StringVar()
        self.status_var.set("Listo")
        self.status_bar = tk.Label(
            self.root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def get_plaintext(self):
        return self.text_to_encrypt.get("1.0", tk.END).strip()
    
    def set_encrypted_text(self, text):
        self.text_to_decrypt.delete("1.0", tk.END)
        self.text_to_decrypt.insert("1.0", text)
    
    def get_encrypted_text(self):
        return self.text_to_decrypt.get("1.0", tk.END).strip()
    
    def set_decrypted_text(self, text):
        self.text_to_encrypt.delete("1.0", tk.END)
        self.text_to_encrypt.insert("1.0", text)
    
    def update_status(self, message):
        self.status_var.set(message)
