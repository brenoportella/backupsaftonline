import pyfiglet


def start(text):
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)
