import os
import threading
from tkinter import messagebox

import backupsaftonline.main as bp
from backupsaftonline.credentials import save_credentials
from backupsaftonline.interface.colors import *


class InterfaceFunc:
    def __init__(self, interface):
        self.interface = interface
        self.is_processing = False
        self.shutdown_flag = threading.Event()

    def open_pdf_with_edge(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'GUIA BPSAFTONLINE.pdf')
        if file_path:
            os.system(f'start msedge "{file_path}"')

    def contact(self):
        messagebox.showinfo(
            'Contacto', 'Envie um e-mail para breno.portella@bwv.pt'
        )

    def start_backup(self):
        if not self.is_processing:
            self.update_progress(0, 0, 0)
            self.is_processing = True
            self.interface.progressbar.configure(
                progress_color=hover_roxo, border_color=preto
            )
            self.interface.progress_label.configure(text_color=preto)
            email = self.interface.login_entry.get()
            password = self.interface.pwd_entry.get()
            save_credentials(email, password)

            try:
                backup = bp.Backup(self.shutdown_flag)
                backup.core(self.update_progress)
            finally:
                messagebox.showinfo(
                    'CONCLUÍDO', 'O processo foi finalizado com exito.'
                )
                self.is_processing = False
        else:
            self.is_processing_alert()

    def run_start_backup(self):
        self.shutdown_flag.clear()
        threading.Thread(target=self.start_backup).start()

    def is_processing_alert(self):
        messagebox.showwarning('ATENÇÃO', 'O processo já está em execução.')

    def stop_backup(self):
        self.shutdown_flag.set()

    def update_progress(self, value, i, qntd):
        self.interface.root.after(
            0, lambda: self.interface.progressbar.set(value / 100)
        )
        self.interface.root.after(
            0,
            lambda: self.interface.progress_label.configure(
                text=f'{i} / {qntd}'
            ),
        )
