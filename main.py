import tkinter as tk

from controllers.main_controller import MainController

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Encriptation Manager")
    app = MainController(root)
    root.mainloop()
