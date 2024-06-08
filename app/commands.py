from abc import ABC, abstractmethod
from app.file import FileProcessor as fp
from app.color import check_txt, color, command_help


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
        return check_txt('bye')


class Hello(Command):
    def execute(self) -> str:
        return check_txt('hello')


class Help(Command):
    def execute(self) -> str:
        return command_help()


class WrongCommand(Command):
    def execute(self):
        return check_txt("invalid command")


class Add(Command):
    def __init__(self, contacts, args) -> None:
        self.contacts = contacts
        self.args = args

    def execute(self) -> str:
        return color(self.contacts.add_record(self.args), 'yellow') + '\n'


class AddBirthday(Command):
    def __init__(self, contacts, args) -> None:
        self.contacts = contacts
        self.args = args

    def execute(self):
        name, date = self.args
        return color(self.contacts.birthday_date(name, date), 'yellow') + '\n'

class Change(Command):
    def __init__(self, contacts, *args) -> None:
        self.contacts = contacts
        self.args = args

    def execute(self):
        return color(self.contacts.change_phone(self.args), 'yellow') + '\n'


class Delete(Command):
    def __init__(self, contacts, args) -> None:
        self.contacts = contacts
        self.args = args

    def execute(self):
        return color(self.contacts.delete(self.args), 'yellow') + '\n'


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
        return color(self.contacts.show_birth_date(self.args), 'green') + '\n'


class Birthdays(Command):
    def __init__(self, contacts) -> None:
        self.contacts = contacts

    def execute(self):
        return self.contacts.get_upcoming_birthdays() + '\n'
