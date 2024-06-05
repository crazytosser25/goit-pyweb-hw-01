"""imports"""
from collections import UserDict
from app.functions import Decorators


class PhonesManager(UserDict):
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
