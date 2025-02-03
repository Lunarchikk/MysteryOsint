# DEOBFUSCATED BY HYPER X SQUAD >>> TOP 1 
# @decoded_softs

import os
import colorama
from colorama import init, Fore
import shutil
import requests
import termcolor
from termcolor import colored
import webbrowser

url = 'https://t.me/decoded_softs'
webbrowser.open(url)
os.system('cls' if os.name == 'nt' else 'clear')

banner = '\n     ███▄ ▄███▓▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███ ▓██   ██▓\n    ▓██▒▀█▀ ██▒ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒██  ██▒\n    ▓██    ▓██░  ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒ ▒██ ██░\n    ▒██    ▒██   ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄   ░ ▐██▓░\n    ▒██▒   ░██▒  ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒ ░ ██▒▓░\n    ░ ▒░   ░  ░   ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░  ██▒▒▒ \n    ░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░         ░     ░░   ░ ▒ ▒ ░░  \n           ░    ░ ░           ░              ░  ░   ░     ░ ░     \n                ░ ░                                       ░ ░     \n    Owner: XYILO\n    Price: NOT Free\n    Version: CRCK Mini Osint\n'
print(colored(banner, 'magenta'))

main = '     Поиск по OSINT\n    ╔════════════════════════════════╗\n    ║[1] - Начать поиск              ║\n    ║[99] - Выход                    ║\n    ╚════════════════════════════════╝'
print(colored(main, 'magenta'))


def center_text(text):
    columns = shutil.get_terminal_size().columns
    lines = text.splitlines()
    centered_lines = [line.center(columns) for line in lines]
    return '\n'.join(centered_lines)


def send_osint_request(query):
    url = f'https://reveng.ee/api/search?q={query}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f'    HTTP error occurred: {err}')
        return {}
    except Exception as err:
        print(f'    An error occurred: {err}')
        return {}


def format_results(results):
    if not results or 'results' not in results:
        return

    for entry in results['results']:
        properties = entry.get('properties', {})
        sources = entry.get('source', [])
        source_names = ', '.join(source['name'] for source in sources)

        print(Fore.MAGENTA + f'   ID: {entry["id"]}')
        print(Fore.MAGENTA + f'   Схема: {entry["schema"]}')

        if properties.get('name'):
            print(Fore.WHITE + '   ├ Полное Имя: ' + ', '.join(properties['name']))
        if properties.get('firstName'):
            print(Fore.WHITE + '   ├ Имя: ' + ', '.join(properties['firstName']))
        if properties.get('lastName'):
            print(Fore.WHITE + '   ├ Фамилия: ' + ', '.join(properties['lastName']))
        if properties.get('fatherName'):
             print(Fore.WHITE + '   ├ Отчество: ' + ', '.join(properties['fatherName']))
        if properties.get('birthDate'):
            print(Fore.WHITE + '   ├ Дата рождения: ' + ', '.join(properties['birthDate']))
        if properties.get('country'):
            print(Fore.WHITE + '   ├ Страна: ' + ', '.join(properties['country']))
        if properties.get('email'):
            print(Fore.WHITE + '   ├ Почта: ' + ', '.join(properties['email']))
        if properties.get('phone'):
            print(Fore.WHITE + '   ├ Телефон: ' + ', '.join(properties['phone']))
        if properties.get('address'):
            print(Fore.WHITE + '   ├ Адрес: ' + ', '.join(properties['address']))
        if properties.get('addressEntity'):
            print(Fore.WHITE + '   ├ Адресная сущность: ' + ', '.join(properties['addressEntity']))
        if properties.get('position'):
            print(Fore.WHITE + '   ├ Должность: ' + ', '.join(properties['position']))
        if properties.get('education'):
            print(Fore.WHITE + '   ├ Образование: ' + ', '.join(properties['education']))
        if properties.get('passportNumber'):
             print(Fore.WHITE + '   ├ Номер паспорта: ' + ', '.join(properties['passportNumber']))
        if properties.get('citizenship'):
            print(Fore.WHITE + '   ├ Гражданство: ' + ', '.join(properties['citizenship']))
        if properties.get('User    account'):
            print(Fore.WHITE + '   ├ Учетная запись пользователя: ' + ', '.join(properties['User    account']))
        if properties.get('Street address'):
            print(Fore.WHITE + '   ├ Улица: ' + ', '.join(properties['Street address']))
        if properties.get('City'):
            print(Fore.WHITE + '   ├ Город: ' + ', '.join(properties['City']))
        if properties.get('Full address'):
             print(Fore.WHITE + '   ├ Полный адрес: ' + ', '.join(properties['Full address']))
        if properties.get('Ownership'):
             print(Fore.WHITE + '   ├ Владение: ' + ', '.join(properties['Ownership']))
        if properties.get('Asset'):
            print(Fore.WHITE + '   ├ Актив: ' + ', '.join(properties['Asset']))
        if properties.get('Document number'):
             print(Fore.WHITE + '   ├ Номер документа: ' + ', '.join(properties['Document number']))
        if properties.get('Type'):
             print(Fore.WHITE + '   ├ Тип: ' + ', '.join(properties['Type']))
        if properties.get('INN'):
             print(Fore.WHITE + '   ├ ИНН: ' + ', '.join(properties['INN']))
        print(Fore.MAGENTA + '--------------------------------------------------')

def main_menu():
    choice = input('   Выберите опцию: ')
    return choice

def start_osint():
    while True:
        choice = main_menu()
        if choice == '99':
            print('Выход из программы.')
            return
        if choice == '1':
            query = input('Введите запрос: ')
            results = send_osint_request(query)
            format_results(results)

if __name__ == '__main__':
    init(autoreset=True)
    start_osint()