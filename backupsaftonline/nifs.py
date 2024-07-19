def nifs(file):
    """
    Reads a text file and extracts a list of NIFs (tax identification numbers).

    This function opens the specified text file, reads each line, strips any
    leading or trailing whitespace, and returns a list of NIFs.

    Args:
        file (str): The path to the text file containing the NIFs.

    Returns:
        list: A list of NIFs read from the file.
    """
    with open(file, 'r') as txt:
        nifs = [line.strip() for line in txt.readlines()]
    return nifs
