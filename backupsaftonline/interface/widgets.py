import tkinter as tk

import customtkinter as ctk

from backupsaftonline.credentials import load_credentials
from backupsaftonline.interface.colors import *


class Widgets:
    @staticmethod
    def widgets(interface):
        creds = load_credentials()
        email = creds.get('email', '')
        password = creds.get('password', '')

        interface.titleLB = ctk.CTkLabel(
            interface.frame_1,
            text='Backup SaftOnline',
            font=('Montserrat Bold', 32),
            text_color=preto,
            anchor='n',
        )
        interface.titleLB.place(relx=0, rely=0.05, relwidth=1)

        interface.login_entryLB = ctk.CTkLabel(
            interface.frame_1,
            text='Login',
            font=('Montserrat Bold', 14),
            text_color=preto,
        )
        interface.login_entryLB.place(relx=0.25, rely=0.26)
        interface.login_entry = ctk.CTkEntry(
            interface.frame_1,
            fg_color=branco,
            text_color=preto,
            placeholder_text_color=place_holder,
            placeholder_text='email@email.pt',
            font=('Montserrat', 12),
        )
        interface.login_entry.insert(0, email)
        interface.login_entry.place(
            relx=0.25, rely=0.30, relheight=0.04, relwidth=0.48
        )

        interface.pwd_entryLB = ctk.CTkLabel(
            interface.frame_1,
            text='Palavra Passe',
            font=('Montserrat Bold', 14),
            text_color=preto,
        )
        interface.pwd_entryLB.place(relx=0.25, rely=0.34)
        interface.pwd_entry = ctk.CTkEntry(
            interface.frame_1,
            fg_color=branco,
            text_color=preto,
            placeholder_text_color=place_holder,
            placeholder_text='password',
            font=('Montserrat', 12),
            show='*',
        )
        interface.pwd_entry.insert(0, password)
        interface.pwd_entry.place(
            relx=0.25, rely=0.38, relheight=0.04, relwidth=0.48
        )

        interface.start_bt = ctk.CTkButton(
            interface.frame_1,
            text='START',
            font=('Montserrat Semibold', 20),
            text_color=branco,
            fg_color=roxo,
            hover_color=hover_roxo,
            corner_radius=30,
            anchor='c',
            command=interface.run_start_backup,
        )
        interface.start_bt.place(
            relx=0.38, rely=0.62, relheight=0.08, relwidth=0.24
        )

        interface.label_guide = ctk.CTkLabel(
            interface.frame_1,
            text='Em caso de duvidas, consulte o tutorial \nno menu superior.',
            font=('Montserrat Light', 14),
            text_color=preto,
            anchor='n',
        )
        interface.label_guide.place(
            relx=0, rely=0.8, relheight=0.08, relwidth=1
        )

    @staticmethod
    def options_menu(interface):
        interface.menu_bar = tk.Menu(interface.root)

        interface.file_menu = tk.Menu(interface.menu_bar, tearoff=0)
        interface.file_menu.add_command(
            label='Guia', command=interface.interface_func.open_pdf_with_edge
        )

        interface.help_menu = tk.Menu(interface.menu_bar, tearoff=0)
        interface.help_menu.add_command(
            label='E-mail', command=interface.interface_func.contact
        )

        interface.menu_bar.add_cascade(
            label='Tutorial', menu=interface.file_menu
        )
        interface.menu_bar.add_cascade(
            label='Contato', menu=interface.help_menu
        )

        interface.root.config(menu=interface.menu_bar)
