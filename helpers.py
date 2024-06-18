import os
import re
import platform

def clean_screen():
    os.system('cls') if platform.system() == 'Windows' else os.system('clear')


def read_text(min_length=0, max_length=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        text = input('> ')
        if len(text) >= min_length and len(text) <= max_length:
            return text

def validate_dni(dni,list):
    if not re.match('[0-9]{2}[A-Z]$',dni):
        print('Invalid dni')
        return False
    for client in list:
        if client.dni == dni:
            print('DNI already exists')
            return False
    return True
