import threading

from backupsaftonline.interface.frames import Frames
from backupsaftonline.interface.interface_func import InterfaceFunc
from backupsaftonline.interface.widgets import Widgets


class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title('Backup SaftOnline')
        self.root.geometry('480x648')
        self.root.resizable(0, 0)

        self.interface_func = InterfaceFunc(self)
        self.frames = Frames.frames(self, root)
        self.widgets = Widgets.widgets(self)
        self.widgets = Widgets.options_menu(self)

    def run_start_backup(self):
        self.interface_func.run_start_backup()


# CASO PRECISE ATUALIZAR A UI USAR ESSE METODO
# def update_ui_callback(self, message):
#     print(message)
