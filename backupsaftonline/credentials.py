# credentials.py
import json
import os

CREDENTIALS_FILE = 'credentials.json'


def load_credentials():
    """Carrega credenciais de um arquivo JSON e retorna um dicionário."""
    if os.path.exists('credentials.json'):
        with open('credentials.json', 'r') as file:
            try:
                data = json.load(file)
                return {
                    'email': data.get('email', ''),
                    'password': data.get('password', '')
                }
            except json.JSONDecodeError:
                return {'email': '', 'password': ''}
    return {'email': '', 'password': ''}

def save_credentials(email, password):
    with open(CREDENTIALS_FILE, 'w') as file:
        json.dump({"email": email, "password": password}, file)