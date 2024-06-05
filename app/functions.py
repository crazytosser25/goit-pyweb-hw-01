"""imports"""
from datetime import datetime
from app.color import color
from app.record import Record

class Decorators:
    """Collection of decorators for AddressBook
    """
    @staticmethod
    def validate_one_arg(func):
        """Decorator to validate functions with 1 argument."""
        def inner(contacts, args):
            if len(args) != 1:
                return 'no name for search'
            contact_name = args[0]
            if contact_name not in contacts:
                return 'phone not in contacts'
            return func(contacts, contact_name)

        return inner

    @staticmethod
    def validate_two_args(func):
        """Decorator to validate functions with 2 arguments."""
        def inner(contacts, args):
            if len(args) != 2:
                return 'invalid args'
            phone = args[1]
            if len(phone) != 10:
                return f'invalid phone {phone}'
            return func(contacts, args)

        return inner

    @staticmethod
    def validate_birthday(func):
        """Decorator to validate functions with 2 arguments."""
        def inner(contacts, args):
            if len(args) != 2:
                return 'invalid args'
            name = args[0]
            date = args[1]
            try:
                datetime.strptime(date, "%d.%m.%Y")
                return func(contacts, name, date)
            except ValueError:
                return f"{color("Date doesn't exist", 'red')}"

        return inner

    @staticmethod
    def validate_three_args(func):
        """Decorator to validate functions with 3 arguments."""
        def inner(contacts, *args):
            if len(args) != 3:
                return 'invalid args'
            phone1, phone2 = args[1], args[2]
            if len(phone1) != 10 and len(phone2) != 10:
                return 'invalid phones.'
            return func(contacts, *args)

        return inner

    @staticmethod
    def make_record(func):
        """A decorator that creates a new contact record and adds
        a phone number to it before calling the decorated function.

        Args:
            func (function): The function to be decorated. It should accept
                two arguments:
                    - contacts: The contact list or dictionary.
                    - new_record: The newly created Record object.
        """
        def inner(contacts, args):
            new_name, new_phone = args
            new_record = Record(new_name)
            new_record.add_phone(new_phone)
            return func(contacts, new_record)

        return inner
