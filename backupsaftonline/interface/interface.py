from backupsaftonline.interface.frames import Frames
from backupsaftonline.interface.widgets import Widgets


class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title('Backup SaftOnline')
        self.root.geometry('480x648')
        self.root.resizable(0, 0)

        self.frames = Frames.frames(self, root)
        self.widgets = Widgets.widgets(self)
        self.widgets = Widgets.options_menu(self)