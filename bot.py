"""imports"""
import re
from pathlib import Path
from app.file import read_file, write_file
from app.color import check_txt, color, command_help


def parse_input(user_input: str) -> tuple:
    """Split the user's input into command and arguments.
        
    Args:
        user_input (str): User input string.

    Returns:
        tuple: A tuple containing the command and its arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    cmd = re.sub("[^A-Za-z]", "", cmd)
    return cmd, *args

def main():
    """This code is designed to create a simple command-line interface (CLI)
    application that interacts with a contacts database. The user can perform
    actions such as adding, changing, and viewing contact information. The CLI
    uses the 'colorama' module to add colors to the output strings for better
    readability.
    """
    database = Path("app/contacts.pkl")
    contacts = read_file(database)

    print(check_txt('greeting'))

    while True:
        user_input = input(check_txt('placeholder'))
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                write_file(database, contacts)
                print(check_txt('bye'))
                break
            case "hello":
                print(check_txt('hello'))
            case "help":
                print(command_help())
            case "add":
                print(color(contacts.add_record(args), 'yellow'), '\n')
            case "addbirthday":
                print(color(contacts.birthday_date(args), 'yellow'), '\n')
            case "change":
                print(color(contacts.change_phone(*args), 'yellow'), '\n')
            case "del":
                print(color(contacts.delete(args), 'yellow'), '\n')
            case "phone":
                print(contacts.find(args))
            case "all":
                print(contacts.show_all())
            case "showbirthday":
                print(color(contacts.show_birth_date(args), 'green'), '\n')
            case "birthdays":
                print(contacts.get_upcoming_birthdays(), '\n')
            case _:
                print(check_txt("invalid command"))


if __name__ == "__main__":
    main()
