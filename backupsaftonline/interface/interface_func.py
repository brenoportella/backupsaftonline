import os
from tkinter import messagebox
from backupsaftonline.credentials import save_credentials
import backupsaftonline.main as bp

class InterfaceFunc:
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
        email = self.login_entry.get()
        password = self.pwd_entry.get()
        save_credentials(email, password)  # Salvar credenciais

        backup = bp.Backup()
        backup.core()