from backupsaftonline.main import Backup
from backupsaftonline.start import start


def main():
    start('BACKUP SAFTONLINE')
    bp = Backup()
    bp.core()


if __name__ == '__main__':
    main()
