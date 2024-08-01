import os
import threading
from tkinter import messagebox

import backupsaftonline.main as bp
from backupsaftonline.credentials import save_credentials


class InterfaceFunc:
    def __init__(self, interface):
        self.interface = interface

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
        email = self.interface.login_entry.get()
        password = self.interface.pwd_entry.get()
        save_credentials(email, password)  # Salvar credenciais

        backup = bp.Backup()
        backup.core()

        # Após o backup ser concluído, atualize a UI
        # self.interface.update_ui_callback('Backup completed!')

    def run_start_backup(self):
        threading.Thread(target=self.start_backup).start()
