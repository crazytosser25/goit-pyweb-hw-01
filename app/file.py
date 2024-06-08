"""imports"""
import pickle
from app.book import AddressBook

class FileException(Exception):
    """Custom exception to handle problems if file is missing or not readable

    Args:
        Exception (any)
    """


class FileProcessor:
    """_summary_"""
    @staticmethod
    def __read_file_check(func) -> callable:
        """Decorator to handle file not found errors."""
        def inner(*args):
            try:
                return func(*args)
            except FileNotFoundError:
                book = AddressBook()
                return book

        return inner

    @staticmethod
    @__read_file_check
    def read_file(database, cipher) -> dict:
        """Read the contents of a ciphered file containing contacts.
            
            Returns:
                dict: A dictionary representing the contacts with names as keys
                and phone numbers as values.
            """
        with open(database, 'rb') as file:
            ciphered_dict = file.read()
        try:
            decrypted_dict = cipher.decrypt_data(ciphered_dict)
        except FileException:
            return 'wrong pass'
        contacts_dict = pickle.loads(decrypted_dict)
        return contacts_dict

    @staticmethod
    def write_file(database, contacts_dict: dict, cipher) -> None:
        """Writes the given dictionary of contacts to a file, with encryption.

            Args:
                contacts_dict (dict): A dictionary representing the contacts,
                with names as keys and phone numbers as values.
            """
        serialized_data = pickle.dumps(contacts_dict)
        ciphered_dict = cipher.encrypt_data(serialized_data)
        with open(database, 'wb') as file:
            file.write(ciphered_dict)
