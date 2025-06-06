import os
from tkinter import filedialog, messagebox
from models.steg_model import SteganographyModel
from views.steg_view import SteganographyView

class SteganographyController:
    def __init__(self, root):
        self.root = root
        self.model = SteganographyModel()
        self.view = SteganographyView(root, self)
    
    def browse_image(self):
        path = filedialog.askopenfilename(
            title="Seleccionar imagen PNG",
            filetypes=[("Imágenes PNG", "*.png")],
            parent=self.root
        )
        if path:
            self.view.set_image_path(path)
            # Sugerir nombre para imagen de salida
            base, ext = os.path.splitext(path)
            self.view.set_output_image(f"{base}_hidden{ext}")
    
    def browse_file_to_hide(self):
        path = filedialog.askopenfilename(
            title="Seleccionar archivo a ocultar",
            parent=self.root
        )
        if path:
            self.view.set_file_to_hide(path)
    
    def browse_output_image(self):
        path = filedialog.asksaveasfilename(
            title="Guardar imagen con archivo oculto",
            defaultextension=".png",
            filetypes=[("Imágenes PNG", "*.png")],
            parent=self.root
        )
        if path:
            self.view.set_output_image(path)
    
    def browse_steg_image(self):
        path = filedialog.askopenfilename(
            title="Seleccionar imagen con datos ocultos",
            filetypes=[("Imágenes PNG", "*.png")],
            parent=self.root
        )
        if path:
            self.view.set_steg_image(path)
            # Verificar si tiene datos ocultos
            if self.model.check_for_hidden_data(path):
                self.view.update_status("Imagen contiene datos ocultos")
            else:
                self.view.update_status("Imagen NO contiene datos ocultos")
    
    def browse_extract_output(self):
        path = filedialog.asksaveasfilename(
            title="Guardar archivo extraído",
            parent=self.root
        )
        if path:
            self.view.set_extracted_file(path)
    
    def hide_file(self):
        image_path = self.view.get_image_path()
        file_to_hide = self.view.get_file_to_hide()
        output_path = self.view.get_output_image()
        
        if not all([image_path, file_to_hide, output_path]):
            self.view.show_error("Complete todos los campos")
            return
        
        try:
            result_path = self.model.hide_file(image_path, file_to_hide, output_path)
            self.view.show_message("Éxito", f"Archivo ocultado correctamente en:\n{result_path}")
            self.view.update_status(f"Archivo ocultado en {os.path.basename(result_path)}")
        except Exception as e:
            self.view.show_error(f"Error ocultando archivo: {str(e)}")
    
    def extract_file(self):
        steg_image = self.view.get_steg_image()
        
        if not steg_image:
            self.view.show_error("Seleccione una imagen con datos ocultos")
            return
        
        try:
            # Extraer automáticamente en el mismo directorio que la imagen
            result_path = self.model.extract_file(steg_image)
            self.view.show_message("Éxito", f"Archivo extraído correctamente en:\n{result_path}")
            self.view.update_status(f"Archivo extraído: {os.path.basename(result_path)}")
        except Exception as e:
            self.view.show_error(f"Error extrayendo archivo: {str(e)}")
