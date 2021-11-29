"""
COMP.CS.100 Programming 1
6.8 Capitalize initial letters of words.
Jani Ollenberg
H288244
"""
def capitalize_initial_letters(text):
    """
    Capitalize initial letter of words using .title
    :param text: string
    :return: string"""
    return text.title()
def main():
    print(capitalize_initial_letters("drIVING cAR"))
if __name__ == "__main__":
    main()