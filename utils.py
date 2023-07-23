import configparser
from console_ui import *

ini_file = "config.ini"


def checking_for_a_number(in_line):
    if not in_line.isdigit() and int(in_line) not in range(get_menu_count()):
        print("Вы ввели некорректные данные. Повторите попытку")
        return False
    else:
        return True


def in_line(message):
    return input(message)


def get_id():
    config = configparser.ConfigParser()
    config.read(ini_file)
    return config["INCREMENTED"]["id"]


def increment_id(id):
    id += 1
    config = configparser.ConfigParser()
    config.read(ini_file)
    config.set("INCREMENTED", "id", str(id))
    with open(ini_file, 'w') as config_file:
        config.write(config_file)


def get_menu_count():
    config = configparser.ConfigParser()
    config.read(ini_file)
    return config["SETTINGS"]["menu_count"]


def show_question(in_message, out_message):
    question = in_line(in_message)
    if question == "y":
        return in_line(out_message)
    elif question == "n":
        return ""
    else:
        show_question(in_message, out_message)