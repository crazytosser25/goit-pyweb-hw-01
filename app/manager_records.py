"""imports"""
from collections import UserDict
from app.functions import Decorators
import app.record as rec

class RecordManager(UserDict):
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
