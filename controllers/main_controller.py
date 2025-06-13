from views.main_view import MainView
from controllers.rsa_controller import RSAController
from controllers.aes_controller import AESController
from controllers.sha256_controller import SHA256Controller
from controllers.steg_controller import SteganographyController
from controllers.bitEdit_controller import BitEditController

import tkinter as tk

class MainController:
    def __init__(self, root):
        self.root = root
        self.view = MainView(root, self)
    
    def open_bit_edit(self):
        bit_edit_window = tk.Toplevel(self.root)
        BitEditController(bit_edit_window)

    def open_rsa(self):
        rsa_window = tk.Toplevel(self.root)
        RSAController(rsa_window)
    
    def open_aes(self):
        aes_window = tk.Toplevel(self.root)
        AESController(aes_window)
    
    def open_sha256(self):
        sha_window = tk.Toplevel(self.root)
        SHA256Controller(sha_window)
    
    def open_steganography(self):
        steg_window = tk.Toplevel(self.root)
        SteganographyController(steg_window)
