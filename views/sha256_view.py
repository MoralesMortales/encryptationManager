import tkinter as tk
from tkinter import ttk, filedialog

class SHA256View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.create_widgets()
    
    def create_widgets(self):
        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack()
        
        # Pestañas
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña de Hash
        self.tab_hash = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_hash, text="Generar Hash")
        
        # Pestaña de Archivos
        self.tab_files = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_files, text="Proteger Archivos")
        
        # --- Contenido pestaña Hash ---
        self.create_hash_tab()
        
        # --- Contenido pestaña Archivos ---
        self.create_files_tab()
        
        # Barra de estado
        self.status_var = tk.StringVar()
        self.status_var.set("Listo")
        self.status_bar = tk.Label(
            self.root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def create_hash_tab(self):
        """Widgets para la pestaña de generación de hash"""
        # Área de texto original
        text_frame = ttk.LabelFrame(self.tab_hash, text="Texto", padding=10)
        text_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.text_input = tk.Text(text_frame, height=5, width=50)
        self.text_input.pack(fill=tk.BOTH, expand=True)
        
        # Botones de acción
        btn_frame = ttk.Frame(self.tab_hash)
        btn_frame.pack(fill=tk.X, pady=5)
        
        self.btn_generate = ttk.Button(btn_frame, text="Generar Hash", width=15)
        self.btn_generate.pack(side=tk.LEFT, padx=5)
        
        self.btn_verify = ttk.Button(btn_frame, text="Verificar", width=15)
        self.btn_verify.pack(side=tk.LEFT, padx=5)
        
        self.btn_clear = ttk.Button(btn_frame, text="Limpiar", width=15)
        self.btn_clear.pack(side=tk.LEFT, padx=5)
        
        # Área de resultado
        result_frame = ttk.LabelFrame(self.tab_hash, text="Hash SHA-256", padding=10)
        result_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.hash_var = tk.StringVar()
        self.hash_entry = ttk.Entry(result_frame, textvariable=self.hash_var, width=64)
        self.hash_entry.pack(fill=tk.X)
    
    def create_files_tab(self):
        """Widgets para la pestaña de protección de archivos"""
        # Frame para selección de archivo
        file_frame = ttk.LabelFrame(self.tab_files, text="Archivo", padding=10)
        file_frame.pack(fill=tk.X, pady=5)
        
        self.file_path_var = tk.StringVar()
        self.file_entry = ttk.Entry(file_frame, textvariable=self.file_path_var)
        self.file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.btn_browse = ttk.Button(file_frame, text="Examinar", width=10)
        self.btn_browse.pack(side=tk.RIGHT)
        
        # Frame para contraseña
        pass_frame = ttk.LabelFrame(self.tab_files, text="Contraseña", padding=10)
        pass_frame.pack(fill=tk.X, pady=5)
        
        self.pass_var = tk.StringVar()
        self.pass_entry = ttk.Entry(pass_frame, textvariable=self.pass_var, show="*")
        self.pass_entry.pack(fill=tk.X)
        
        # Botones de acción
        action_frame = ttk.Frame(self.tab_files)
        action_frame.pack(fill=tk.X, pady=10)
        
        self.btn_encrypt_file = ttk.Button(action_frame, text="Encriptar Archivo", width=20)
        self.btn_encrypt_file.pack(side=tk.LEFT, padx=5)
        
        self.btn_decrypt_file = ttk.Button(action_frame, text="Desencriptar Archivo", width=20)
        self.btn_decrypt_file.pack(side=tk.LEFT, padx=5)
    
    def get_text(self):
        return self.text_input.get("1.0", tk.END).strip()
    
    def set_hash(self, hash_value):
        self.hash_var.set(hash_value)
    
    def get_hash(self):
        return self.hash_var.get()
    
    def clear_all(self):
        self.text_input.delete("1.0", tk.END)
        self.hash_var.set("")
    
    def get_file_path(self):
        return self.file_path_var.get()
    
    def set_file_path(self, path):
        self.file_path_var.set(path)
    
    def get_password(self):
        return self.pass_var.get()
    
    def update_status(self, message):
        self.status_var.set(message)
    
    def ask_file(self):
        return filedialog.askopenfilename(title="Seleccionar archivo", parent=self.root)
    
    def show_message(self, title, message):
        tk.messagebox.showinfo(title, message, parent=self.root)
    
    def show_error(self, message):
        tk.messagebox.showerror("Error", message, parent=self.root)
