import tkinter as tk
from tkinter import ttk

class AESView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.create_widgets()
    
    def create_widgets(self):
        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack()
        
        # Key Management
        self.key_frame = tk.LabelFrame(self.main_frame, text="Gestión de Clave AES", padx=10, pady=10)
        self.key_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.key_label = tk.Label(self.key_frame, text="Clave AES (base64):")
        self.key_label.pack(side=tk.LEFT)
        
        self.key_var = tk.StringVar()
        self.key_entry = tk.Entry(self.key_frame, textvariable=self.key_var, width=50)
        self.key_entry.pack(side=tk.LEFT, padx=5)
        
        # Frame para botones de clave
        self.key_btn_frame = tk.Frame(self.key_frame)
        self.key_btn_frame.pack(side=tk.LEFT, padx=5)
        
        self.btn_generate = tk.Button(self.key_btn_frame, text="Generar Nueva", width=12)
        self.btn_generate.pack(pady=2)
        
        self.btn_save_key = tk.Button(self.key_btn_frame, text="Guardar Clave", width=12)
        self.btn_save_key.pack(pady=2)
        
        # Área de texto para encriptar
        self.encrypt_frame = tk.LabelFrame(self.main_frame, text="Encriptar", padx=10, pady=10)
        self.encrypt_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=(0, 5))
        
        self.text_to_encrypt = tk.Text(self.encrypt_frame, height=10, width=40)
        self.text_to_encrypt.pack()
        
        self.btn_encrypt = tk.Button(self.encrypt_frame, text="Encriptar")
        self.btn_encrypt.pack(pady=(10, 0))
        
        # Área de texto para desencriptar
        self.decrypt_frame = tk.LabelFrame(self.main_frame, text="Desencriptar", padx=10, pady=10)
        self.decrypt_frame.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT, padx=(5, 0))
        
        self.text_to_decrypt = tk.Text(self.decrypt_frame, height=10, width=40)
        self.text_to_decrypt.pack()
        
        self.btn_decrypt = tk.Button(self.decrypt_frame, text="Desencriptar")
        self.btn_decrypt.pack(pady=(10, 0))
        
        # Barra de estado
        self.status_var = tk.StringVar()
        self.status_var.set("Listo")
        self.status_bar = tk.Label(
            self.root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def update_key_display(self, key_b64):
        self.key_var.set(key_b64)
    
    def update_status(self, message):
        self.status_var.set(message)
    
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
