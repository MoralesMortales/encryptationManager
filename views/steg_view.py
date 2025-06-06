import tkinter as tk
from tkinter import ttk

class SteganographyView:
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
        
        # Pestaña para ocultar
        self.tab_hide = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_hide, text="Ocultar Archivo")
        
        # Pestaña para extraer
        self.tab_extract = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_extract, text="Extraer Archivo")
        
        # Widgets para ocultar
        self.create_hide_tab()
        
        # Widgets para extraer
        self.create_extract_tab()
        
        # Barra de estado
        self.status_var = tk.StringVar()
        self.status_var.set("Listo")
        self.status_bar = tk.Label(
            self.root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def create_hide_tab(self):
        """Widgets para ocultar archivos"""
        frame = ttk.LabelFrame(self.tab_hide, text="Ocultar archivo en imagen", padding=10)
        frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Imagen portadora
        ttk.Label(frame, text="Imagen PNG:").grid(row=0, column=0, sticky="w")
        self.image_path_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.image_path_var, width=40).grid(row=0, column=1, sticky="ew")
        ttk.Button(frame, text="Examinar", command=self.controller.browse_image).grid(row=0, column=2, padx=5)
        
        # Archivo a ocultar
        ttk.Label(frame, text="Archivo a ocultar:").grid(row=1, column=0, sticky="w")
        self.file_to_hide_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.file_to_hide_var, width=40).grid(row=1, column=1, sticky="ew")
        ttk.Button(frame, text="Examinar", command=self.controller.browse_file_to_hide).grid(row=1, column=2, padx=5)
        
        # Imagen de salida
        ttk.Label(frame, text="Imagen de salida:").grid(row=2, column=0, sticky="w")
        self.output_image_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.output_image_var, width=40).grid(row=2, column=1, sticky="ew")
        ttk.Button(frame, text="Examinar", command=self.controller.browse_output_image).grid(row=2, column=2, padx=5)
        
        # Botón de acción
        ttk.Button(frame, text="Ocultar Archivo", command=self.controller.hide_file).grid(row=3, column=1, pady=10)
    
    def create_extract_tab(self):
        """Widgets para extraer archivos (ahora sin seleccionar ruta)"""
        frame = ttk.LabelFrame(self.tab_extract, text="Extraer archivo de imagen", padding=10)
        frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Imagen con datos ocultos
        ttk.Label(frame, text="Imagen con datos:").grid(row=0, column=0, sticky="w")
        self.steg_image_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.steg_image_var, width=40).grid(row=0, column=1, sticky="ew")
        ttk.Button(frame, text="Examinar", command=self.controller.browse_steg_image).grid(row=0, column=2, padx=5)
        
        # Botón de acción (ahora sin selección de destino)
        ttk.Button(frame, text="Extraer Archivo", command=self.controller.extract_file).grid(row=1, column=1, pady=10)
    
    def set_image_path(self, path):
        self.image_path_var.set(path)
    
    def set_file_to_hide(self, path):
        self.file_to_hide_var.set(path)
    
    def set_output_image(self, path):
        self.output_image_var.set(path)
    
    def set_steg_image(self, path):
        self.steg_image_var.set(path)
    
    def set_extracted_file(self, path):
        self.extracted_file_var.set(path)
    
    def get_image_path(self):
        return self.image_path_var.get()
    
    def get_file_to_hide(self):
        return self.file_to_hide_var.get()
    
    def get_output_image(self):
        return self.output_image_var.get()
    
    def get_steg_image(self):
        return self.steg_image_var.get()
    
    def get_extracted_file(self):
        return self.extracted_file_var.get()
    
    def update_status(self, message):
        self.status_var.set(message)
    
    def show_message(self, title, message):
        tk.messagebox.showinfo(title, message, parent=self.root)
    
    def show_error(self, message):
        tk.messagebox.showerror("Error", message, parent=self.root)
