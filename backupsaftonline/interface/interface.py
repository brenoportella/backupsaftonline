from backupsaftonline.interface.frames import frames
from backupsaftonline.interface.widgets import options_menu, widgets


class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title('Backup SaftOnline')
        self.root.geometry('480x648')
        self.root.resizable(0, 0)

        self.frames = frames(self)
        self.widgets = widgets(self)
        self.options_menu = options_menu(self)
