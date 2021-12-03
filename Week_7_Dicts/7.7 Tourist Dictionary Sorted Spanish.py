"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.
Jani Ollenberg
H288244
"""
def print_dictionary(dictionary):
    """
    Sorts and prints all words in dictionary separated by comma.
    :param dictionary: dict containing all words
    """
    print("Dictionary contents:")
    all_words = ", ".join(sorted(dictionary))
    print(all_words)
def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    print_dictionary(english_spanish)

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                translated = english_spanish[word]
                print(f"{word} in Spanish is {translated}")
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            english = input("Give the word to be added in English: ")
            spanish = input("Give the word to be added in Spanish: ")
            english_spanish[english] = spanish
            print_dictionary(english_spanish)
        elif command == "R":
            remove = input("Give the word to be removed: ")
            if remove in english_spanish:
                del english_spanish[remove]
            else:
                print(f"The word {remove} could not be found from the dictionary.")
        elif command == "Q":
            print("Adios!")
            return
        elif command == "P":
            print()
            print("English-Spanish")
            for words in sorted(english_spanish):
                print(words, english_spanish[words])
            spanish_english = {}
            for key in english_spanish:
                spanish_english[english_spanish[key]] = key
            print()
            print("Spanish-English")
            for words in sorted(spanish_english):
                print(words, spanish_english[words])
            print()
        elif command == "T":
            text = input("Enter the text to be translated into Spanish: ")
            words_list = text.split()
            print("The text, translated by the dictionary:")
            for word in words_list:
                if word in english_spanish:
                    print(english_spanish[word], end=" ")
                else:
                    print(word, end=" ")
            print()    
        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
