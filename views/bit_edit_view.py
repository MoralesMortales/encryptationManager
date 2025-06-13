import tkinter as tk
from tkinter import ttk

class BitEditView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.create_widgets()
    
    def create_widgets(self):
        self.root.title("BitEdit - Editor de Bits de Archivos")
        self.root.geometry("600x500")
        
        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # File Management
        self.file_frame = tk.LabelFrame(self.main_frame, text="Gestión de Archivos", padx=10, pady=10)
        self.file_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.btn_load_file = tk.Button(self.file_frame, text="Cargar Archivo")
        self.btn_load_file.pack(side=tk.LEFT, padx=5)
        
        self.btn_save_file = tk.Button(self.file_frame, text="Guardar Copia")
        self.btn_save_file.pack(side=tk.LEFT, padx=5)
        
        self.file_info_label = tk.Label(self.file_frame, text="Ningún archivo cargado")
        self.file_info_label.pack(side=tk.LEFT, padx=10)
        
        # Navigation Section
        self.nav_frame = tk.LabelFrame(self.main_frame, text="Navegación", padx=10, pady=10)
        self.nav_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(self.nav_frame, text="Posición:").pack(side=tk.LEFT)
        self.position_entry = tk.Entry(self.nav_frame, width=10)
        self.position_entry.pack(side=tk.LEFT, padx=5)
        
        self.btn_goto_byte = tk.Button(self.nav_frame, text="Ir a Byte")
        self.btn_goto_byte.pack(side=tk.LEFT, padx=5)
        
        self.btn_prev_byte = tk.Button(self.nav_frame, text="< Anterior")
        self.btn_prev_byte.pack(side=tk.LEFT, padx=5)
        
        self.btn_next_byte = tk.Button(self.nav_frame, text="Siguiente >")
        self.btn_next_byte.pack(side=tk.LEFT, padx=5)
        
        # Byte Editor Section
        self.byte_frame = tk.LabelFrame(self.main_frame, text="Editor de Bytes", padx=10, pady=10)
        self.byte_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        tk.Label(self.byte_frame, text="Valor del Byte (0-255):").pack(anchor=tk.W)
        self.byte_value_entry = tk.Entry(self.byte_frame, width=10)
        self.byte_value_entry.pack(anchor=tk.W, pady=(0, 10))
        
        self.btn_read_byte = tk.Button(self.byte_frame, text="Leer Byte")
        self.btn_read_byte.pack(side=tk.LEFT, padx=5)
        
        self.btn_write_byte = tk.Button(self.byte_frame, text="Escribir Byte")
        self.btn_write_byte.pack(side=tk.LEFT, padx=5)
        
        # Bit Editor Section
        self.bit_frame = tk.LabelFrame(self.byte_frame, text="Editor de Bits", padx=10, pady=10)
        self.bit_frame.pack(fill=tk.X, pady=(10, 0))
        
        tk.Label(self.bit_frame, text="Posición del Bit (0-7):").grid(row=0, column=0, sticky=tk.W)
        self.bit_position_entry = tk.Entry(self.bit_frame, width=5)
        self.bit_position_entry.grid(row=0, column=1, padx=5, sticky=tk.W)
        
        tk.Label(self.bit_frame, text="Valor del Bit (0/1):").grid(row=0, column=2, sticky=tk.W)
        self.bit_value_entry = tk.Entry(self.bit_frame, width=5)
        self.bit_value_entry.grid(row=0, column=3, padx=5, sticky=tk.W)
        
        self.btn_set_bit = tk.Button(self.bit_frame, text="Modificar Bit")
        self.btn_set_bit.grid(row=0, column=4, padx=5)
        
        # Binary Representation
        self.binary_frame = tk.Frame(self.byte_frame)
        self.binary_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.bit_labels = []
        for i in range(8):
            frame = tk.Frame(self.binary_frame, bd=1, relief=tk.SUNKEN)
            frame.pack(side=tk.LEFT, padx=2)
            
            tk.Label(frame, text=f"Bit {7-i}").pack()
            label = tk.Label(frame, text="0", font=("Courier", 12, "bold"))
            label.pack()
            self.bit_labels.append(label)
        
        # Status Bar
        self.status_var = tk.StringVar()
        self.status_var.set("Listo")
        self.status_bar = tk.Label(
            self.root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def get_position(self):
        return self.position_entry.get()
    
    def set_position(self, position):
        self.position_entry.delete(0, tk.END)
        self.position_entry.insert(0, position)
    
    def get_byte_value(self):
        return self.byte_value_entry.get()
    
    def set_byte_value(self, value):
        self.byte_value_entry.delete(0, tk.END)
        self.byte_value_entry.insert(0, str(value))
        
        # Actualizar representación binaria
        for i in range(8):
            bit = (value >> (7-i)) & 1
            self.bit_labels[i].config(text=str(bit))
    
    def get_bit_position(self):
        return self.bit_position_entry.get()
    
    def get_bit_value(self):
        return self.bit_value_entry.get()
    
    def set_file_info(self, info):
        self.file_info_label.config(text=info)
    
    def update_status(self, message):
        self.status_var.set(message)
