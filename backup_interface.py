import customtkinter as ctk

from backupsaftonline.interface.interface import Interface

if __name__ == '__main__':
    root = ctk.CTk()

    app = Interface(root)
    root.after(300, root.mainloop())
