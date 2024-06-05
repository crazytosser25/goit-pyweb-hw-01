"""imports"""
from app.manager_records import RecordManager
from app.manager_phones import PhonesManager
from app.manager_birthdays import BirthdayManager


class Singleton:
    """Singleton parent class for AddressBook"""
    __instance = None
    def __new__(cls):
        if not isinstance(cls.__instance, cls):
            cls.__instance = object.__new__(cls)
        return cls.__instance


class AddressBook(Singleton):
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

    def __init__(self):
        self.contacts = RecordManager()
        self.phones = PhonesManager()
        self.birthdays = BirthdayManager()

    def add_record(self, user_record):
        return self.contacts.add_record(user_record)

    def find(self, contact_name):
        return self.contacts.find(contact_name)

    def show_all(self):
        return self.contacts.show_all()

    def add_phone(self, contact_name, new_phone):
        return self.phones.add_phone(contact_name, new_phone)

    def change_phone(self, contact_name, old_phone, new_phone):
        return self.phones.change_phone(contact_name, old_phone, new_phone)

    def find_by_phone(self, phone_number):
        return self.phones.find_by_phone(phone_number)

    def birthday_date(self, contact_name, birth_date):
        return self.birthdays.birthday_date(contact_name, birth_date)

    def show_birth_date(self, contact_name):
        return self.birthdays.show_birth_date(contact_name)

    def get_upcoming_birthdays(self, days=7):
        return self.birthdays.get_upcoming_birthdays(days)

    def delete(self, contact_name):
        return self.contacts.delete(contact_name)
