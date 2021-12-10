"""
A program for managing a small phone book. The phone book entries are stored
in a text file.
"""

# Commands known to the program as global constants.
ADD_COMMAND = "1"
UPDATE_COMMAND = "2"
REMOVE_COMMAND = "3"
PRINT_COMMAND = "4"
LOAD_COMMAND = "5"
SAVE_COMMAND = "6"
QUIT_COMMAND = "7"

# An error message for an missing element as a global constant.
MISSING_MESSAGE = "Name not in the phone book!"

# A message for an error that happens during the loading or saving of a file
# as a global constant.
FILE_ERROR_MESSAGE = "File processing error!"

def add_entry(phone_book):
    """Add a new entry to the phone book, if it is not already in the book.

    :param name: dict, the phone book.
    """
    # Read the inputs from the user.
    name = input("Enter a name: ")
    phone_number = input("Enter a phone number: ")

    # Add to the phone book.
    if name not in phone_book:
        phone_book[name] = phone_number
    # Print an error message.
    else:
        print("Entry already in the phone book!")

def update_entry(phone_book):
    """Update a phone number, if it is in the book.

    :param name: dict, the phone book.
    """
    # Read the inputs from the user.
    name = input("Enter a name: ")
    phone_number = input("Enter a new phone number: ")

    # Update the number.
    if name in phone_book:
        phone_book[name] = phone_number
    # Print an error message.
    else:
        print(MISSING_MESSAGE)

def remove_entry(phone_book):
    """Remove an entry from the phone book, if it is in the book.

    :param name: dict, the phone book.
    """
    # Read the name from the user.
    name = input("Enter a name: ")

    # Remove from the book.
    if name in phone_book:
        del phone_book[name]
    # Print an error message.
    else:
        print(MISSING_MESSAGE)

def read_choice():
    """Read a choice from the user and return it.

    :return: str, user's choice.
    """
    # Let us assume that the user is in wrong, as always.
    invalid_input = True

    # Read input, while it is invalid.
    while invalid_input:
        msg = ADD_COMMAND + ") Add, " + UPDATE_COMMAND + ") Update, " + \
        REMOVE_COMMAND + ") Remove, " + PRINT_COMMAND + ") Print, " + \
        LOAD_COMMAND + ") Load, " + SAVE_COMMAND + ") Save and " + \
        QUIT_COMMAND + ") Quit: "
        print(msg)
        choice = input("Please, enter your selection: ")
        # A shorter alternative for a conditional expression applying
        # comparisons and logical operators.
        if choice in (ADD_COMMAND, UPDATE_COMMAND, REMOVE_COMMAND,
        PRINT_COMMAND, LOAD_COMMAND, SAVE_COMMAND, QUIT_COMMAND):
            invalid_input = False
        else:
            print("Invalid choice!")

    # Return user's choice.
    return choice

def print_book(phone_book):
    """Print the phone book. Does nothing, if the book is empty.

    :param name: dict, the phone book.
    """
    for name in phone_book:
        print(name, phone_book[name])

def load_book(file_name):
    """Tries to load the phone book entries from a text file. It is assumed
    that each line of the file has one entry and that the line consists of
    the name and the phone number separated with a comma.

    :param file_name: str, the name of the file containing the entries.
    :return: dict, the phone book containing the entries, if the the file can
    be opened and the entries read from the file. The return value is None,
    if an exception is raised.
    """
    try:
        # Try to open the file for the reading of the entries.
        book_file = open(file_name, mode = "r")

        # Initialize the a dictionary for the entries.
        phone_book = {}

        # Populate the dictionary, until the file has been processed.
        for line in book_file:
            # Remove the character(s) that end the line.
            line = line.rstrip()

            # Split the line in two.
            name, phone_number = line.split(",")

            # Add a new entry to the phone book.
            phone_book[name] = phone_number

        # Close the file.
        book_file.close()
    except OSError:
        # Make a note of an error.
        print(FILE_ERROR_MESSAGE)
        phone_book = None

    # Return the entries or the error code.
    return phone_book

def save_book(file_name, phone_book):
    """Tries to save the phone book entries into a text file. A line in
    the file has one entry. The line consists of the name and the phone
    number separated with a comma.

    :param file_name: str, the name of the file containing the entries.
    :param name: dict, the phone book.
    """
    try:
        # Try to open the file for the saving of the entries.
        book_file = open(file_name, mode = "w")

        # Save entries to the file. The print function separates the data
        # and ends the line.
        for name in phone_book:
            line = name + "," + phone_book[name]
            print(line, file = book_file)

        # Close the file.
        book_file.close()
    except OSError:
        # Make a note of an error.
        print(FILE_ERROR_MESSAGE)

def main():
    # The name of the file containing the entries of the phone book.
    PHONE_BOOK_FILE_NAME = "phonebook.txt"

    # The book is empty at the start.
    phone_book = {}

    # Call functions until the user has had enough.
    do_the_loop = True
    while do_the_loop:
        # Decide what to do.
        choice = read_choice()
        if choice == ADD_COMMAND:
            add_entry(phone_book)
        elif choice == UPDATE_COMMAND:
            update_entry(phone_book)
        elif choice == REMOVE_COMMAND:
            remove_entry(phone_book)
        elif choice == PRINT_COMMAND:
            print_book(phone_book)
        elif choice == LOAD_COMMAND:
            # Try to load the entries in a dictionary and assing a temporary
            # reference to the return value.
            new_phone_book = load_book(PHONE_BOOK_FILE_NAME)
            # Assign the new dictionary to the local variable, if no exception
            # is raised, while the file is loaded.
            if new_phone_book != None:
                phone_book = new_phone_book
        elif choice == SAVE_COMMAND:
            save_book(PHONE_BOOK_FILE_NAME, phone_book)
        elif choice == QUIT_COMMAND:
            do_the_loop = False

if __name__ == "__main__":
    main()
