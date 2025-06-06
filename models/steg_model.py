import os
class SteganographyModel:
    def __init__(self):
        self.marker = b'STEG_MARKER:'
        self.metadata_marker = b'METADATA:'  # Nuevo marcador para metadatos

    def hide_file(self, image_path, file_to_hide, output_path):
        """Oculta un archivo dentro de una imagen PNG, guardando su nombre original"""
        if not os.path.exists(image_path):
            raise FileNotFoundError("La imagen no existe")
        if not os.path.exists(file_to_hide):
            raise FileNotFoundError("El archivo a ocultar no existe")
        
        with open(image_path, 'rb') as img_file:
            img_data = img_file.read()
        
        if img_data[-8:] != b'IEND\xaeB`\x82':
            raise ValueError("El archivo no es un PNG válido")
        
        # Obtener nombre y extensión original
        original_filename = os.path.basename(file_to_hide)
        with open(file_to_hide, 'rb') as secret_file:
            secret_data = secret_file.read()
        
        # Añadir metadatos (nombre original) antes del contenido
        metadata = self.metadata_marker + original_filename.encode('utf-8') + b'|'
        combined_data = img_data[:-8] + self.marker + metadata + secret_data + img_data[-8:]
        
        with open(output_path, 'wb') as output_file:
            output_file.write(combined_data)
        
        return output_path

    def extract_file(self, image_path, output_dir=None):
        """Extrae un archivo oculto de una imagen PNG, usando su nombre original"""
        if not os.path.exists(image_path):
            raise FileNotFoundError("La imagen no existe")
        
        with open(image_path, 'rb') as img_file:
            img_data = img_file.read()
        
        if self.marker not in img_data:
            raise ValueError("No se encontraron datos ocultos en la imagen")
        
        # Extraer datos ocultos (incluyendo metadatos si existen)
        hidden_data = img_data.split(self.marker)[1].split(b'IEND\xaeB`\x82')[0]
        
        # Verificar si hay metadatos
        if self.metadata_marker in hidden_data:
            # Separar metadatos y contenido real
            metadata_part = hidden_data.split(self.metadata_marker)[1]
            original_filename, secret_data = metadata_part.split(b'|', 1)
            original_filename = original_filename.decode('utf-8')
        else:
            # Si no hay metadatos, usar un nombre por defecto
            original_filename = "archivo_extraido.dat"
            secret_data = hidden_data
        
        # Si no se especifica directorio de salida, usar el mismo de la imagen
        if output_dir is None:
            output_dir = os.path.dirname(image_path)
        
        output_path = os.path.join(output_dir, original_filename)
        
        # Guardar el archivo extraído
        with open(output_path, 'wb') as secret_file:
            secret_file.write(secret_data)
        
        return output_path

    def check_for_hidden_data(self, image_path):
        """Verifica si una imagen contiene datos ocultos"""
        try:
            with open(image_path, 'rb') as f:
                data = f.read()
                return self.marker in data
        except:
            return False
