"""imports"""
try:
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)
    COLORAMA = True
except ImportError:
    COLORAMA = False


def check_txt(arg: str) -> str:
    """Function for easy access to class ColorTxt.

    Args:
        arg (str): Takes str to match case in class.

    Returns:
        str: Colored or not text for output.
    """
    output = ColorTxt()
    return output(arg)

def color(args: str, chosen_color: str) -> str:
    """Function to color text output in color if 'colorama' imported."""
    if not COLORAMA:
        return args
    match chosen_color:
        case 'yellow':
            return f"{Fore.YELLOW}{args}"
        case 'green':
            return f"{Fore.GREEN}{args}"
        case 'cyan':
            return f"{Fore.CYAN}{args}"
        case 'red':
            return f"{Fore.RED}{args}"

def command_help():
    """Help for commands of bot"""
    return "'add [name] [phone]'\t\t\tto add new contact " \
            "(phone must be 10 digits).\n" \
            "'add-birthday [name] [birth date]'\tto add date" \
            "of birth (date must be in format 'DD.MM.YYYY').\n" \
            "'all'\t\t\t\t\tto review all contacts.\n" \
            "'birthdays'\t\t\t\tto show upcoming birthdays in 7 days.\n" \
            "'change [name] [old phone] [new phone]'\t" \
            "to change contact's phone number.\n" \
            "'del [name]'\t\t\t\tto delete contact from list.\n" \
            "'phone [name]'\t\t\t\tto review contact's phone number.\n" \
            "'show-birthday [name]'\t\t\tto show birth date of contact.\n" \
            "'close' or 'exit'\t\t\tto exit assistant.\n"


class ColorTxt:
    """Colorized output in case of user input, output and mistakes."""
    def __call__(self, arg):
        return self.colored_txt(arg) if COLORAMA else self.formatted_txt(arg)

    def colored_txt(self, request: str) -> str:
        """Colorized output in case of user input, output and mistakes.

    This function takes a single argument, `request` which is a string
    representing a message. It returns a formatted string with colorful
    terminal output based on the given request.

    Args:
        request (str): The message to be displayed.

    Returns:
        str: A formatted string containing the error message in colorful
        terminal output.
    """
        match request:
            case 'greeting':
                return f"\n{Fore.YELLOW}Welcome to the assistant bot!\n" \
                "(enter 'help' for list of commands)\n"
            case 'placeholder':
                return f"Enter a command: {Fore.BLUE}"
            case 'bye':
                return f"{Fore.YELLOW}Good bye!\n"
            case 'hello':
                return f"{Fore.YELLOW}How can I help you?\n"
            case 'invalid command':
                return f"{Fore.RED}Invalid command.\n"
            case 'phone not in contacts':
                return f"{Fore.RED}Invalid Name.\n{Fore.YELLOW}This contact " \
                    "doesn't exist."
            case 'contact exists':
                return f"{Fore.RED}Invalid Name.\n{Fore.YELLOW}This contact " \
                    "already exists."
            case 'no name for search':
                return f"{Fore.RED}Invalid data.\n{Fore.YELLOW}You must " \
                    "give me Name."
            case 'invalid phone':
                return f"{Fore.RED}Invalid Phone-number.\n{Fore.YELLOW}Must " \
                    "be 10 numbers."
            case 'invalid args':
                return f"{Fore.RED}Invalid data.\n{Fore.YELLOW}You must " \
                    "give me Name and Phone-number."

    def formatted_txt(self, request: str) -> str:
        """Non-colorized output in case of user input, output and mistakes.

    This function takes a single argument, `request` which is a string
    representing a message. It returns a formatted string based on the given
    request.

    Args:
        request (str): The message to be displayed.

    Returns:
        str: A formatted string containing the error message in colorful
        terminal output.
    """
        match request:
            case 'greeting':
                return "\nWelcome to the assistant bot!\n" \
                "(enter 'help' for list of commands)\n"
            case 'placeholder':
                return "Enter a command: "
            case 'bye':
                return "Good bye!\n"
            case 'hello':
                return "How can I help you?\n"
            case 'invalid command':
                return "Invalid command.\n"
            case 'phone not in contacts':
                return "Invalid Name.\nThis contact " \
                    "doesn't exist."
            case 'contact exists':
                return "Invalid Name.\nThis contact " \
                    "already exists."
            case 'no name for search':
                return "Invalid data.\nYou must " \
                    "give me Name."
            case 'invalid phone':
                return "Invalid Phone-number.\nMust " \
                    "be 10 numbers."
            case 'invalid args':
                return "Invalid data.\nYou must " \
                    "give me Name and Phone-number."
