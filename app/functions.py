"""imports"""
from datetime import datetime, timedelta
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


def find_next_weekday(start_date, weekday) -> datetime:
    """Finds the date of the next specified weekday after the given start date.

    Args:
        start_date (datetime): The date from which to start the search.
        weekday (int): The desired weekday as an integer,
        where Monday is 0 and Sunday is 6.

    Returns:
        datetime: The date of the next specified weekday after the start date.
    """
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday: datetime) -> datetime:
    """Adjusts the birthday date to the next Monday if it falls on a weekend.

    Args:
        birthday (datetime): The birthday date to adjust.

    Returns:
        datetime: The adjusted birthday date, or the original date if it
            falls on a weekday.
    """
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday

def date_to_string(date: datetime) -> str:
    """Converts a datetime object to a string representation
    in the format 'DD.MM.YYYY'.

    Args:
        date (datetime): The datetime object to convert.

    Returns:
        str: The string representation of the date in the format 'DD.MM.YYYY'.
    """
    try:
        return date.strftime("%d.%m.%Y")
    except AttributeError:
        return 'No date added.'

def stringify_birthdays(list_of_birthdays: list) -> str:
    """Creates a formatted string representation of a list of birthdays.

    Args:
        list_of_birthdays (list): A list of dictionaries containing 'name'
            and 'congratulation_date' keys.

    Returns:
        str: A formatted string representing the list of birthdays.

    Example:
        >birthdays = [{'name': 'John Doe', 'congratulation_date': '31-12-2024'}, 
        >           {'name': 'Jane Smith', 'congratulation_date': '01-01-2025'}]
        >stringify_birthdays(birthdays)
        'John Doe......................31-12-2024'
        'Jane Smith...................01-01-2025'
    """
    output_string = ''
    for item in list_of_birthdays:
        output_string += f"{color(item['name'], 'green').ljust(30, '.')}" \
                        f"{color(item['congratulation_date'], 'cyan')}\n"
    return output_string
