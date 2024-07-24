import tkinter as tk

import customtkinter as ctk

from backupsaftonline.interface.interface_func import \
    InterfaceFunc as interfaceF

from backupsaftonline.interface.colors import *

import backupsaftonline.main as bp

from backupsaftonline.credentials import load_credentials



def widgets(self):
    
    backup = bp.Backup()
    
    creds = load_credentials()  
    email = creds.get('email', '')  
    password = creds.get('password', '')

    self.titleLB = ctk.CTkLabel(
        self.frame_1,
        text='Backup SaftOnline',
        font=('Montserrat Bold', 32),
        text_color=preto,
        anchor='n',
    )
    self.titleLB.place(relx=0, rely=0.05, relwidth=1)

    self.login_entryLB = ctk.CTkLabel(
        self.frame_1,
        text='Login',
        font=('Montserrat Bold', 14),
        text_color=preto,
    )
    self.login_entryLB.place(relx=0.25, rely=0.26)
    self.login_entry = ctk.CTkEntry(
        self.frame_1,
        fg_color=branco,
        text_color=preto,
        placeholder_text_color=place_holder,
        placeholder_text='email@email.pt',
        font=('Montserrat', 12),
    )
    self.login_entry.insert(0, email)
    self.login_entry.place(relx=0.25, rely=0.30, relheight=0.04, relwidth=0.48)

    self.pwd_entryLB = ctk.CTkLabel(
        self.frame_1,
        text='Palavra Passe',
        font=('Montserrat Bold', 14),
        text_color=preto,
    )
    self.pwd_entryLB.place(relx=0.25, rely=0.34)
    self.pwd_entry = ctk.CTkEntry(
        self.frame_1,
        fg_color=branco,
        text_color=preto,
        placeholder_text_color=place_holder,
        placeholder_text='password',
        font=('Montserrat', 12),
        show='*',
    )
    self.pwd_entry.insert(0, password)
    self.pwd_entry.place(relx=0.25, rely=0.38, relheight=0.04, relwidth=0.48)

    self.start_bt = ctk.CTkButton(
        self.frame_1,
        text='START',
        font=('Montserrat Semibold', 20),
        text_color=branco,
        fg_color=roxo,
        hover_color=hover_roxo,
        corner_radius=30,
        anchor='c',
        command=lambda: (interfaceF.start_backup(self)),
    )  # aqui coloca o programa da MAIN para rodar.
    self.start_bt.place(relx=0.38, rely=0.62, relheight=0.08, relwidth=0.24)

    self.label_guide = ctk.CTkLabel(
        self.frame_1,
        text='Em caso de duvidas, consulte o tutorial \nno menu superior.',
        font=('Montserrat Light', 14),
        text_color=preto,
        anchor='n',
    )
    self.label_guide.place(relx=0, rely=0.8, relheight=0.08, relwidth=1)


def options_menu(self):
    self.menu_bar = tk.Menu(self.root)

    self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
    self.file_menu.add_command(
        label='Guia', command=lambda: (interfaceF.open_pdf_with_edge(self))
    )

    self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
    self.help_menu.add_command(
        label='E-mail', command=lambda: (interfaceF.contact(self))
    )

    self.menu_bar.add_cascade(label='Tutorial', menu=self.file_menu)
    self.menu_bar.add_cascade(label='Contato', menu=self.help_menu)

    self.root.config(menu=self.menu_bar)
