"""imports"""
from collections import UserDict
from datetime import date
from app.functions import (Decorators,
                        adjust_for_weekend,
                        date_to_string,
                        stringify_birthdays
                    )
import app.record as rec


class Singleton:
    """Singleton parent class for AddressBook"""
    __instance = None
    def __new__(cls):
        if not isinstance(cls.__instance, cls):
            cls.__instance = object.__new__(cls)
        return cls.__instance


class AddressBook(Singleton, UserDict):
    """A simple Singleton address book implementation.

    This class extends the UserDict class to manage a collection of contacts.
    Uses classes: Name and Phone (children of Field) to store data, and
    Record to manage phone numbers.

    Args:
        UserDict (_type_): A class from the 'collections' module.

    Methods:
        - add_record: Add a new contact record to the address book.
        - find: Find a contact record by name.
        - find_by_phone: Find a contact record by phone number.
        - delete: Delete a contact record from the address book.
    """

    @Decorators.validate_two_args
    @Decorators.make_record
    def add_record(self, user_record: rec.Record) -> str:
        """Add a new contact record to the address book.

        Args:
            user_record (Record): The contact record to be added.

        Returns:
            str: A message indicating the status of the operation.
        """
        if user_record.name.value in self.data:
            return 'contact exists'
        self.data[user_record.name.value] = user_record
        return "Contact added."

    @Decorators.validate_one_arg
    def find(self, contact_name: str) -> str:
        """Finding a contact record by name.

        Args:
            contact_name (str): The name of the contact to search for.

        Returns:
            str: The contact record corresponding to the provided name.
        """
        return self.data[contact_name]

    def find_by_phone(self, phone_number: str) -> str:
        """Find a contact record by phone number.

        Args:
            phone_number (str): The phone number to search for.

        Returns:
            str: The name of the contact associated with given phone number.
        """
        for contact_name, phone_record in self.data.items():
            if phone_record.find_phone(phone_number):
                return contact_name
        return "No contact found with this phone number"

    @Decorators.validate_two_args
    def add_phone(self, contact_name, new_phone):
        """Adds a new phone number to the specified contact.

        Args:
            contact_name (str): The name of the contact to whom the phone
                number will be added.
            new_phone (str): The new phone number to add to the contact.

        Returns:
            bool: True if the phone was successfully added, False otherwise.
        """
        return self.data[contact_name].add_phone(new_phone)

    @Decorators.validate_three_args
    def change_phone(self, contact_name, old_phone, new_phone):
        """Changes an existing phone number for the specified contact.

        Args:
            contact_name (str): The name of the contact whose phone number
                will be changed.
            old_phone (str): The old phone number that needs to be replaced.
            new_phone (str): The new phone number that will replace the old one.

        Returns:
            bool: True if the phone was successfully changed, False otherwise.
        """
        return self.data[contact_name].edit_phone(old_phone, new_phone)

    def show_all(self) -> str:
        """Display all the contacts.

    Args:
        contacts (dict): A dictionary containing contacts base.

    Returns:
        str: The formatted list of contacts.
    """
        output_of_contacts: str = ''
        for _, phone_record in self.data.items():
            output_of_contacts += f"{phone_record}\n"
        return output_of_contacts

    @Decorators.validate_birthday
    def birthday_date(self, contact_name, birth_date):
        """Adds a birthday date to the specified contact.

        Args:
            contact_name (str): The name of the contact to whom the birthday
                date will be added.
            birth_date (str): The birthday date to add to the contact.
                The format should be 'DD-MM-YYYY'.

        Returns:
            bool: True if the birthday was successfully added, False otherwise.
        """
        return self.data[contact_name].add_birthday(birth_date)

    @Decorators.validate_one_arg
    def show_birth_date(self, contact_name):
        """Retrieves and returns the birthday date of the specified contact
        as a string.

        Args:
            contact_name (str): The name of the contact whose birthday date
                will be retrieved.

        Returns:
            str: The birthday date of the contact in string format.
        """
        return date_to_string(self.data[contact_name].show_birthday())

    def get_upcoming_birthdays(self, days=7):
        """Retrieves and returns a list of upcoming birthdays within
        the specified number of days.

        Args:
            days (int, optional): The number of days ahead to check for
                upcoming birthdays. Defaults to 7.

        Returns:
            str: A formatted string listing the upcoming birthdays within
                the specified number of days, or a message indicating
                no expected birthdays.

        """
        upcoming_birthdays = []
        today = date.today()

        for user, _ in self.data.items():
            birth_date = self.data[user].show_birthday()
            try:
                birthday_this_year = birth_date.replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = birth_date.replace(year=today.year+1)
            except TypeError:
                continue

            if 0 <= (birthday_this_year - today).days <= days:
                birthday_this_year = adjust_for_weekend(birthday_this_year)
                congratulation_date_str = date_to_string(birthday_this_year)
                upcoming_birthdays.append({
                    "name": user,
                    "congratulation_date": congratulation_date_str
                })
        if upcoming_birthdays:
            return stringify_birthdays(upcoming_birthdays)
        return 'No birthdays exspected next week.'

    @Decorators.validate_one_arg
    def delete(self, contact_name: str) -> str:
        """Delete a contact record from the address book.

        Args:
            contact_name (str): The name of the contact to be deleted.

        Returns:
            str: A message indicating the status of the operation.
        """
        if contact_name not in self.data:
            return "Contact not found"
        del self.data[contact_name]
        return "Contact deleted"
