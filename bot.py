"""imports"""
import re
import sys
from pathlib import Path
from app.file import FileProcessor as fp
from app.protection import Cipher
from app.interface import CommandLineInterface
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
        password = interface.asking("Please, enter password to AddressBook: ")
        cryptograph = Cipher(password)
        contacts = fp.read_file(base, cryptograph)
        if contacts != 'wrong pass':
            return contacts, cryptograph
        interface.answer(
            f"Incorrect password. {2 - attempt} attempts left."
        )
    interface.answer("Access denied.")
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
        sys.exit()
    interface.answer("Welcome to the assistant bot!\n" \
                "(enter 'help' for list of commands)\n")
    working = True

    while working:
        user_input = interface.asking("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                message = cmd.Close(database, contacts, cryptograph)
                working = False
            case "hello":
                message = cmd.Hello()
            case "help":
                message = cmd.Help()
            case "add":
                message = cmd.Add(contacts, args)
            case "addbirthday":
                message = cmd.AddBirthday(contacts, args)
            case "change":
                message = cmd.Change(contacts, *args)
            case "del":
                message = cmd.Delete(contacts, args)
            case "phone":
                message = cmd.Phone(contacts, args)
            case "all":
                message = cmd.All(contacts)
            case "showbirthday":
                message = cmd.ShowBirthday(contacts, args)
            case "birthdays":
                message = cmd.Birthdays(contacts)
            case _:
                message = cmd.WrongCommand()
        interface.answer(message.execute())


if __name__ == "__main__":
    main()
