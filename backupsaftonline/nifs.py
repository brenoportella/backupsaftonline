def nifs(file):
    with open(file, 'r') as file:
        nifs = [line.strip() for line in file.readlines()]
    return nifs
