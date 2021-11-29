"""
COMP.CS.100 Programming 1
6.7 Create acronyms of words.
Jani Ollenberg
H288244
"""
def create_an_acronym(text):
    """
    Create an acronym of given text.
    :param text: text to use
    :return: acronymized text
    """
    split = text.split()
    acronym = ""
    for word in split:
        acronym += word[0] 
    return acronym.upper()
def main():
    acronym = create_an_acronym("tampere u n iversity")
    print(acronym)
if __name__ == "__main__":
    main()