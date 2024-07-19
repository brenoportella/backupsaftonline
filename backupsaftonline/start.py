import pyfiglet


def start(text):
    """
    Prints the provided text as ASCII art using the pyfiglet library.

    This function converts the given text into ASCII art and prints it to the console.
    It uses the `figlet_format` function from the pyfiglet library to generate the ASCII art representation.

    Args:
        text (str): The text to be converted into ASCII art and printed.

    Returns:
        None
    """
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)
