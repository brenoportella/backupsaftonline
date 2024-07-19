from backupsaftonline.main import Backup
from backupsaftonline.start import start


def main():
    """
    Main function to initialize the SAFTONLINE backup process.

    This function calls the 'start' function to begin the process with the name 'BACKUP SAFTONLINE'
    and then creates an instance of the 'Backup' class and calls its 'core' method to
    perform the backup.

    Returns:
        None
    """
    start('BACKUP SAFTONLINE')
    bp = Backup()
    bp.core()


if __name__ == '__main__':
    main()
