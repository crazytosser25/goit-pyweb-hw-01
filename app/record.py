"""imports"""
from datetime import datetime
from app.color import color


class Field:
    """Class for storing data of str type"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Class for storing names of contacts. Str type of data."""


class Phone(Field):
    """Class for storing list of phone numbers.
    
    Methods:
        - validate_phone: Validate a phone number format.
    """
    def __init__(self, phone: str):
        self.validate_phone(phone)
        super().__init__(phone)

    def validate_phone(self, phone: str) -> None:
        """Validate a phone number format.

        This method validates the format of a phone number by checking
        its length and whether it consists of digits only. Raises
        ValueError if the phone number format is incorrect.

        Args:
            phone (str): The phone number to validate.
        """
        if len(phone) != 10 or not phone.isdigit():
            raise ValueError('Wrong phone format!')


class Birthday(Field):
    """A class representing a birthday, inheriting from Field.

    Args:
        birth_date (str): The birth date in the format 'DD.MM.YYYY'.

    Attributes:
        birthday (datetime.date): The birthday date object.
    """
    def __init__(self, birth_date: str):
        try:
            self.birthday = datetime.strptime(birth_date, '%d.%m.%Y').date()
            super().__init__(self.birthday)
        except ValueError as e:
            raise ValueError("Invalid date format. Use DD.MM.YYYY") from e


class Record:
    """Class for storing and processing contact records.
    
    Methods:
        - add_phone: Add a phone number to the list of phones.
        - edit_phone: Edit an existing phone number in the list.
        - find_phone: Find a phone number in the list.
        - remove_phone: Remove a phone number from the list.
    """
    def __init__(self, contact_name: str):
        self.name = Name(contact_name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        return (
            f"{color('Contact name: ', 'cyan')}" \
            f"{color(self.name.value, 'green').ljust(30, '.')}" \
            f" phones: " \
            f"{color('; '.join(phone.value for phone in self.phones), 'cyan')}"
        )

    def add_phone(self, phone_number: str) -> None:
        """Add a phone number to the list of phones.

        This method adds a new phone number to the existing list of phones.
        Raises ValueError if the provided phone number is already in the list.

        Args:
            phone_number (str): The phone number to be added.
        """
        if phone_number in [str(phone) for phone in self.phones]:
            return 'This phone already in list'
        self.phones.append(Phone(phone_number))
        return 'Phone added'

    def edit_phone(self, old_number: str, new_number: str):
        """Edit an existing phone number in the list.

        This method allows you to update an existing phone number with 
        a new one in the list of phones.

        Args:
            old_number (str): The current phone number to be replaced.
            new_number (str): The new phone number to replace the old one.
        """
        try:
            Phone(new_number)
        except ValueError:
            return 'New number already in list.'

        for number in self.phones:
            if number.value == old_number:
                number.value = new_number
                break
        return 'Phone changed'

    def find_phone(self, phone_number: str) -> str:
        """Find a phone number in the list.

        This method searches for a given phone number in the list of phones and
        returns it if found.

        Args:
            phone_number (str): The phone number to search for.

        Returns:
            str: The found phone number if it exists in the list;
            otherwise, returns None.
        """
        for number in self.phones:
            if number.value == phone_number:
                return phone_number

    def remove_phone(self, phone: str) -> None:
        """Remove a phone number from the list.

        This method removes the specified phone number from the list of phones.
        Raises ValueError if the provided phone number does not exist 
        in the list.

        Args:
            phone (str): The phone number to be removed.
        """
        self.phones.remove(self.find_phone(phone))

    def add_birthday(self, birth_date: str) -> str:
        """Adds a birthday to the contact if not already present.

        Args:
            birth_date (str): The birth date to add, in the format 'DD.MM.YYYY'.

        Returns:
            str: A message indicating whether the birthday was added or if it
                was already present.
        """
        if self.birthday:
            return "Birthday already written"
        self.birthday = Birthday(birth_date)
        return 'Birthday added.'

    def show_birthday(self) -> datetime:
        """Retrieves and returns the birthday date of the contact.

        Returns:
            datetime: The birthday date of the contact if set.
            str: A message indicating no birthday date is added if not set.

        """
        try:
            return self.birthday.value
        except AttributeError:
            return 'No birthday date added.'
