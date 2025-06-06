import tkinter as tk

class MainView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.create_widgets()
    
    def create_widgets(self):
        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack()
        
        btn_rsa = tk.Button(
            self.frame, 
            text="Encriptador RSA",
            command=self.controller.open_rsa,
            width=20, height=2
        )
        btn_rsa.pack(pady=10)
        
        btn_aes = tk.Button(
            self.frame,
            text="Encriptador AES",
            command=self.controller.open_aes,
            width=20, height=2
        )
        btn_aes.pack(pady=10)
        
        btn_sha = tk.Button(
            self.frame,
            text="Hash SHA-256",
            command=self.controller.open_sha256,
            width=20, height=2
        )
        btn_sha.pack(pady=10)
        
        btn_steg = tk.Button(
            self.frame,
            text="Esteganografía",
            command=self.controller.open_steganography,
            width=20, height=2
        )
        btn_steg.pack(pady=10)
        
        btn_exit = tk.Button(
            self.frame,
            text="Salir",
            command=self.root.quit,
            width=20, height=2
        )
        btn_exit.pack(pady=10)
