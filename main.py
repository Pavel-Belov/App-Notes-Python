import sys

from connamds import *
from console_ui import *
from utils import *


def main():
    try:
        main_menu_ui()

        while 1:
            command = in_line("Введите соответствующую цифру для работы с заметками: ")
            while not checking_for_a_number(command):
                command = in_line("Введите соответствующую цифру для работы с заметками: ")

            if command == "0":
                exit_program()
            else:
                if command == "1":
                    print("----------Создание заметки----------")
                    title = in_line("Введите название заметки: ")
                    text = in_line("Введте текст заметки: ")
                    create_note(title, text)
                    print("")
                elif command == "2":
                    print("----------Удаление заметки----------")
                    id_note = in_line("Введите id для удаления заметки: ")
                    delete_note(id_note)
                    print("")
                elif command == "3":
                    print("----------Редактирование заметки----------")
                    id_note = in_line("Введите id для редаткирования заметки: ")
                    title = show_question("Хотите поменять заголовок заметки (y/n): ",
                                          "Новый заголовок: ")
                    text = show_question("Хотите поменять текст заметки (y/n): ",
                                         "Новый текст: ")
                    edit_note(id_note, title, text)
                    print("")
                elif command == "4":
                    print("----------Просмотр заметки----------")
                    id_note = in_line("Введите id, чтобы посмотреть заметку: ")
                    note = get_note(id_note)
                    if note != None:
                        print(note)
                    else:
                        print("Такой заметки не существует")
                    print("")
                elif command == "5":
                    print("----------Список все заметок----------")
                    notes = get_list_of_notes()
                    print(notes)
                    print("")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


def exit_program():
    print("До новых встреч!...")
    sys.exit(0)


if __name__ == "__main__":
    main()
