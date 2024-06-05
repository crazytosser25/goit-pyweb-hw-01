"""imports"""
from collections import UserDict
from datetime import date, datetime, timedelta
from app.functions import Decorators
from app.color import color


class BirthdayManager(UserDict):
    @staticmethod
    def find_next_weekday(start_date, weekday) -> datetime:
        """Finds the date of the next specified weekday after the given 
        start date.

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

    @staticmethod
    def adjust_for_weekend(birthday: datetime) -> datetime:
        """Adjusts the birthday date to the next Monday if it falls 
        on a weekend.

        Args:
            birthday (datetime): The birthday date to adjust.

        Returns:
            datetime: The adjusted birthday date, or the original date if it
                falls on a weekday.
        """
        if birthday.weekday() >= 5:
            return BirthdayManager.find_next_weekday(birthday, 0)
        return birthday

    @staticmethod
    def date_to_string(formated_date: datetime) -> str:
        """Converts a datetime object to a string representation
        in the format 'DD.MM.YYYY'.

        Args:
            date (datetime): The datetime object to convert.

        Returns:
            str: The string representation of the date in the format 'DD.MM.YYYY'.
        """
        try:
            return formated_date.strftime("%d.%m.%Y")
        except AttributeError:
            return 'No date added.'

    @staticmethod
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
        retrieved_date = self.data[contact_name].show_birthday()
        return BirthdayManager.date_to_string(retrieved_date)

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
                birthday_this_year = BirthdayManager.adjust_for_weekend(
                    birthday_this_year
                )
                congratulation_date_str = BirthdayManager.date_to_string(
                    birthday_this_year
                )
                upcoming_birthdays.append({
                    "name": user,
                    "congratulation_date": congratulation_date_str
                })
        if upcoming_birthdays:
            return BirthdayManager.stringify_birthdays(upcoming_birthdays)
        return 'No birthdays exspected next week.'
