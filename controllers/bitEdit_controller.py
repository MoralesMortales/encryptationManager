from tkinter import messagebox, filedialog
import os
import tkinter as tk
from views.bit_edit_view import BitEditView

class BitEditController:
    def __init__(self, root):
        self.root = root
        self.view = BitEditView(root, self)
        self.setup_commands()
        self.current_file = None
        self.current_position = 0
    
    def setup_commands(self):
        self.view.btn_load_file.config(command=self.load_file)
        self.view.btn_save_file.config(command=self.save_file)
        self.view.btn_goto_byte.config(command=self.goto_byte)
        self.view.btn_read_byte.config(command=self.read_byte)
        self.view.btn_write_byte.config(command=self.write_byte)
        self.view.btn_set_bit.config(command=self.set_bit)
        self.view.btn_next_byte.config(command=self.next_byte)
        self.view.btn_prev_byte.config(command=self.prev_byte)
    
    def load_file(self):
        file_path = filedialog.askopenfilename(
            title="Seleccionar archivo para edición",
            parent=self.root
        )
        if file_path:
            self.current_file = file_path
            self.current_position = 0
            file_size = os.path.getsize(file_path)
            self.view.update_status(f"Archivo cargado: {os.path.basename(file_path)} ({file_size} bytes)")
            self.view.set_file_info(f"Tamaño: {file_size} bytes - Posición actual: 0")
            self.read_byte()
    
    def save_file(self):
        if not self.current_file:
            messagebox.showerror("Error", "No hay archivo cargado", parent=self.root)
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Guardar archivo modificado",
            defaultextension=os.path.splitext(self.current_file)[1],
            initialfile=f"edited_{os.path.basename(self.current_file)}",
            parent=self.root
        )
        
        if file_path:
            try:
                with open(self.current_file, 'rb') as src, open(file_path, 'wb') as dst:
                    dst.write(src.read())
                self.view.update_status(f"Archivo guardado como {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {str(e)}", parent=self.root)
    
    def goto_byte(self):
        if not self.current_file:
            messagebox.showerror("Error", "No hay archivo cargado", parent=self.root)
            return
        
        try:
            position = int(self.view.get_position())
            file_size = os.path.getsize(self.current_file)
            
            if position < 0 or position >= file_size:
                messagebox.showerror("Error", f"Posición inválida. El archivo tiene {file_size} bytes (0-{file_size-1})", parent=self.root)
                return
            
            self.current_position = position
            self.view.set_file_info(f"Posición actual: {position}")
            self.read_byte()
            self.view.update_status(f"Saltando a byte {position}")
        except ValueError:
            messagebox.showerror("Error", "La posición debe ser un número entero", parent=self.root)
    
    def read_byte(self):
        if not self.current_file:
            messagebox.showerror("Error", "No hay archivo cargado", parent=self.root)
            return
        
        try:
            with open(self.current_file, 'rb') as file:
                file.seek(self.current_position)
                byte = file.read(1)
                
                if not byte:
                    messagebox.showwarning("Advertencia", "Fin de archivo alcanzado", parent=self.root)
                    return
                
                byte_value = byte[0]
                self.view.set_byte_value(byte_value)
                self.view.update_status(f"Byte leído en posición {self.current_position}: {byte_value} (0x{byte_value:02X})")
        except Exception as e:
            messagebox.showerror("Error", f"Error al leer byte: {str(e)}", parent=self.root)
    
    def write_byte(self):
        if not self.current_file:
            messagebox.showerror("Error", "No hay archivo cargado", parent=self.root)
            return
        
        try:
            byte_value = int(self.view.get_byte_value())
            
            if byte_value < 0 or byte_value > 255:
                messagebox.showerror("Error", "El valor del byte debe estar entre 0 y 255", parent=self.root)
                return
            
            with open(self.current_file, 'r+b') as file:
                file.seek(self.current_position)
                file.write(bytes([byte_value]))
            
            self.view.update_status(f"Byte modificado en posición {self.current_position}: {byte_value} (0x{byte_value:02X})")
        except ValueError:
            messagebox.showerror("Error", "El valor del byte debe ser un número entre 0 y 255", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Error al escribir byte: {str(e)}", parent=self.root)
    
    def set_bit(self):
        if not self.current_file:
            messagebox.showerror("Error", "No hay archivo cargado", parent=self.root)
            return
        
        try:
            bit_position = int(self.view.get_bit_position())
            bit_value = int(self.view.get_bit_value())
            
            if bit_position < 0 or bit_position > 7:
                messagebox.showerror("Error", "La posición del bit debe estar entre 0 y 7", parent=self.root)
                return
            
            if bit_value not in (0, 1):
                messagebox.showerror("Error", "El valor del bit debe ser 0 o 1", parent=self.root)
                return
            
            with open(self.current_file, 'r+b') as file:
                # Leer el byte actual
                file.seek(self.current_position)
                byte = file.read(1)[0]
                
                # Modificar el bit específico
                mask = 1 << bit_position
                if bit_value:
                    modified_byte = byte | mask   # Setear bit a 1
                else:
                    modified_byte = byte & ~mask  # Setear bit a 0
                
                # Escribir el byte modificado
                file.seek(self.current_position)
                file.write(bytes([modified_byte]))
            
            self.view.update_status(f"Bit {bit_position} modificado a {bit_value} en byte {self.current_position}")
            self.read_byte()  # Actualizar la vista
        except ValueError:
            messagebox.showerror("Error", "Valores inválidos para posición/valor del bit", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Error al modificar bit: {str(e)}", parent=self.root)
    
    def next_byte(self):
        if not self.current_file:
            messagebox.showerror("Error", "No hay archivo cargado", parent=self.root)
            return
        
        file_size = os.path.getsize(self.current_file)
        if self.current_position + 1 >= file_size:
            messagebox.showwarning("Advertencia", "Fin de archivo alcanzado", parent=self.root)
            return
        
        self.current_position += 1
        self.view.set_position(str(self.current_position))
        self.view.set_file_info(f"Posición actual: {self.current_position}")
        self.read_byte()
    
    def prev_byte(self):
        if not self.current_file:
            messagebox.showerror("Error", "No hay archivo cargado", parent=self.root)
            return
        
        if self.current_position <= 0:
            messagebox.showwarning("Advertencia", "Inicio de archivo alcanzado", parent=self.root)
            return
        
        self.current_position -= 1
        self.view.set_position(str(self.current_position))
        self.view.set_file_info(f"Posición actual: {self.current_position}")
        self.read_byte()
