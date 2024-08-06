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
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)

    def run_start_backup(self):
        self.interface_func.run_start_backup()

    def on_closing(self):
        self.interface_func.stop_backup()
        self.root.destroy()
