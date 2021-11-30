"""
COMP.CS.100 Programming 1
6.12 How many abbas in a text
Jani Ollenberg
H288244
"""
def count_abbas(text):
    """
    Count all the occurences of 'abba' in the text.
    :return: int, number of abbas"""
    counter = 0
    if len(text) < 4:
        return 0
    for i in range(len(text)):
        # print(text[i:i+4])
        if 'abba' in text[i:i+4]:
            counter += 1
    return counter
def main():
    print(count_abbas("abbabbabba"))
    print(count_abbas("barbapapa"))
if __name__ == "__main__":
    main()