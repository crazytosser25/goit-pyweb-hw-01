"""imports"""
from abc import ABC, abstractmethod
from app.file import FileProcessor as fp


class Command(ABC):
    @abstractmethod
    def execute(self) -> str:
        pass


class Close(Command):
    def __init__(self, database, contacts, cryptograph) -> None:
        self.database = database
        self.contacts = contacts
        self.cryptograph = cryptograph

    def execute(self) -> str:
        fp.write_file(self.database, self.contacts, self.cryptograph)
        return "Good bye!\n"


class Hello(Command):
    def execute(self) -> str:
        return "How can I help you?\n"


class Help(Command):
    def execute(self) -> str:
        return "'add [name] [phone]'\t\t\tto add new contact " \
            "(phone must be 10 digits).\n" \
            "'add-birthday [name] [birth date]'\tto add date" \
            "of birth (date must be in format 'DD.MM.YYYY').\n" \
            "'all'\t\t\t\t\tto review all contacts.\n" \
            "'birthdays'\t\t\t\tto show upcoming birthdays in 7 days.\n" \
            "'change [name] [old phone] [new phone]'\t" \
            "to change contact's phone number.\n" \
            "'del [name]'\t\t\t\tto delete contact from list.\n" \
            "'phone [name]'\t\t\t\tto review contact's phone number.\n" \
            "'show-birthday [name]'\t\t\tto show birth date of contact.\n" \
            "'close' or 'exit'\t\t\tto exit assistant.\n"


class WrongCommand(Command):
    def execute(self):
        return "Invalid command.\n"


class Add(Command):
    def __init__(self, contacts, args) -> None:
        self.contacts = contacts
        self.args = args

    def execute(self) -> str:
        return f"{self.contacts.add_record(self.args)}\n"

class AddBirthday(Command):
    def __init__(self, contacts, args) -> None:
        self.contacts = contacts
        self.args = args

    def execute(self):
        name, date = self.args
        return f"{self.contacts.birthday_date(name, date)}\n"

class Change(Command):
    def __init__(self, contacts, *args) -> None:
        self.contacts = contacts
        self.args = args

    def execute(self):
        return f"{self.contacts.change_phone(self.args)}\n"


class Delete(Command):
    def __init__(self, contacts, args) -> None:
        self.contacts = contacts
        self.args = args

    def execute(self):
        return f"{self.contacts.delete(self.args)}\n"


class Phone(Command):
    def __init__(self, contacts, args) -> None:
        self.contacts = contacts
        self.args = args

    def execute(self):
        return self.contacts.find(self.args)


class All(Command):
    def __init__(self, contacts) -> None:
        self.contacts = contacts

    def execute(self):
        return self.contacts.show_all()


class ShowBirthday(Command):
    def __init__(self, contacts, args) -> None:
        self.contacts = contacts
        self.args = args

    def execute(self):
        return f"{self.contacts.show_birth_date(self.args)}\n"


class Birthdays(Command):
    def __init__(self, contacts) -> None:
        self.contacts = contacts

    def execute(self):
        return f"{self.contacts.get_upcoming_birthdays()}\n"
