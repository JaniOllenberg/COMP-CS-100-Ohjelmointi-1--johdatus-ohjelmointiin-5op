"""
COMP.CS.100 Programming 1
Code template for the hottest hit song Yogi Bear
Jani Ollenberg
H288244
"""
def verse(verse, animal):
    """
    Print the song verse.
    """
    print(verse)
    print(animal, animal, sep=", ")
    print(verse)
    repeat_name(animal, 3)
    print(verse)
    repeat_name(animal, 1)

def repeat_name(animal, repeats):
    """
    Repeats bear name.
    Parameters = name, how many repeats
    """
    for _ in range(repeats):
        print(f'{animal}, {animal} Bear')

def main():
    verse("I know someone you don't know", "Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
