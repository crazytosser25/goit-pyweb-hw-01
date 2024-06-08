"""imports"""
import re
import sys
from pathlib import Path
from app.file import FileProcessor as fp
from app.protection import Cipher
from app.color import check_txt, color
from app.cli import CommandLineInterface
import app.commands as cmd


database = Path("data/contacts.pkl")
interface = CommandLineInterface()

def password_check(base: Path):
    """ Function to prompt the user for a password and validate it 
        against the database.

    Args:
        database (Path): Path to the file containing the encrypted contacts 
            database.

    Returns:
        Dict, Cipher: AddressBook instance and the corresponding cipher object 
            if the password is correct, or None if access is denied
            after three incorrect attempts.
    """
    for attempt in range(3):
        password = interface.asking('Please, enter password to AddressBook: ')
        cryptograph = Cipher(password)
        contacts = fp.read_file(base, cryptograph)
        if contacts != 'wrong pass':
            return contacts, cryptograph
        print(color(
            f"Incorrect password. {2 - attempt} attempts left.",
            'red'),
            '\n'
        )
    print(color("Access denied.", 'red'))
    return None

def parse_input(user_input: str) -> tuple:
    """Split the user's input into command and arguments.
        
    Args:
        user_input (str): User input string.

    Returns:
        tuple: A tuple containing the command and its arguments.
    """
    command, *args = user_input.split()
    command = command.strip().lower()
    command = re.sub("[^A-Za-z]", "", command)
    return command, *args

def main():
    """This code is designed to create a simple command-line interface (CLI)
    application that interacts with a contacts database. The user can perform
    actions such as adding, changing, and viewing contact information. The CLI
    uses the 'colorama' module to add colors to the output strings for better
    readability and Fernet for encrypting file.
    """
    try:
        contacts, cryptograph = password_check(database)
    except TypeError:
        print('no file')
        sys.exit()
    print(check_txt('greeting'))

    while True:
        user_input = interface.asking(check_txt('placeholder'))
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                message = cmd.Close(database, contacts, cryptograph)
                print(message.execute())
                break
            case "hello":
                message = cmd.Hello()
                print(message.execute())
            case "help":
                message = cmd.Help()
                print(message.execute())
            case "add":
                message = cmd.Add(contacts, args)
                print(message.execute())
            case "addbirthday":
                message = cmd.AddBirthday(contacts, args)
                print(message.execute())
            case "change":
                message = cmd.Change(contacts, *args)
                print(message.execute())
            case "del":
                message = cmd.Delete(contacts, args)
                print(message.execute())
            case "phone":
                message = cmd.Phone(contacts, args)
                print(message.execute())
            case "all":
                message = cmd.All(contacts)
                print(message.execute())
            case "showbirthday":
                message = cmd.ShowBirthday(contacts, args)
                print(message.execute())
            case "birthdays":
                message = cmd.Birthdays(contacts)
                print(message.execute())
            case _:
                message = cmd.WrongCommand()
                print(message.execute())


if __name__ == "__main__":
    main()
