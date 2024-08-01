import customtkinter as ctk
from backupsaftonline.interface.colors import *

class Frames:
    def frames(self, root):
        self.frame_1 = ctk.CTkFrame(root, fg_color= branco)
        self.frame_1.place(relx=0, rely=0, relheight=1, relwidth=1)