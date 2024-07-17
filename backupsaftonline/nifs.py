def nifs():
    with open('./tests/nif_saft.txt', 'r') as file:
        nifs = [line.strip() for line in file.readlines()]
    return nifs