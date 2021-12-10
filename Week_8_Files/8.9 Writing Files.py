"""
COMP.CS.100 Programming 1
Write file with line numbers and text.
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
    filename = input("Enter the name of the file: ")
    try:
        file = open(filename, mode="w")
    except:
        print(f"Writing the file {filename} was not successful.")
        return
    print("Enter rows of text. Quit by entering an empty row.")
    msg = read_message()
    line_number = 1
    for i in msg:
        print(f"{line_number} {i}", file=file)
        line_number += 1
    print(f"File {filename} has been written.")
    file.close()
if __name__ == "__main__":
    main()
