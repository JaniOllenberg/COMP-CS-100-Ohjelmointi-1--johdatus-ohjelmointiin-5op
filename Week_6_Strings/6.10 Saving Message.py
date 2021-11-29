"""
COMP.CS.100 Programming 1
Code Template
Jani Ollenberg
H288244
"""
def read_message():
    """
    Read lines of text from user.
    :return: list of lines
    """
    messages = []
    while True:
        message = input()
        if message == "":
            return messages
        else:
            messages.append(message)
def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("The same, shouting:")
    for i in msg:
        print(i.upper())


if __name__ == "__main__":
    main()
