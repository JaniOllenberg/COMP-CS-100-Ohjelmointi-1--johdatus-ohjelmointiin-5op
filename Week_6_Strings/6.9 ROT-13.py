"""
COMP.CS.100 Programming 1
ROT13 program code template
Jani Ollenberg
H288244
"""

def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    # TODO: implement encryption here
    index = 0
    for char in regular_chars:
        #print(char)
        if text == char:
            # print(f"{char} found this.")
            # print(f"{encrypted_chars[index]} replace with this")
            text = encrypted_chars[index]
            return text
        elif text.lower() == char:
            # print(text.lower())
            text = encrypted_chars[index].upper()
            return text
        index += 1
    return text
def row_encryption(text):
    """
    Encrypt a row of text with ROT-13
    :param text: str
    :return: str
    """
    encrypted = ""
    for char in text:
        encrypted += encrypt(char)
    return encrypted
def main():
    print(encrypt('a'))
    encrypted = row_encryption("Encrypt this text. Then decrypt it back again.")
    print(encrypted)
    decrypted = row_encryption(encrypted)
    print(decrypted)
if __name__ == "__main__":
    main()