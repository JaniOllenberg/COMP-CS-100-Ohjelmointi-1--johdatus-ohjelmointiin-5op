"""
COMP.CS.100 Programming 1
6.4. Count the vowels and consonants in a word.
Jani Ollenberg
H288244
"""
def is_a_vowel(char):
    """
    Checks if character is a vowel.
    :param char: character to check
    :return: bool, True if a vowel
    """
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' \
        or char == 'u' or char == 'y':
        return True
    else:
        return False
def main():
    word = input("Enter a word: ")
    vowels = 0
    consonants = 0
    for i in range(len(word)):
        if is_a_vowel(word[i]):
            vowels += 1
        else:
            consonants += 1
    # Print the beginning of the output. Do not start a new line.
    print(f"The word \"{word}\" contains ", end = "")
    print(f"{vowels} vowels and {consonants} consonants.")
if __name__ == "__main__":
    main()