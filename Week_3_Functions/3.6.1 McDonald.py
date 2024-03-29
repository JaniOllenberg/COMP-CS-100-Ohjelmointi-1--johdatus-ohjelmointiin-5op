"""
COMP.CS.100 Programming 1
Template Song: Old MacDonald
Jani Ollenberg
H288244
"""
def print_verse(animal, sound):
    """
    Prints the song verse.
    Parameters = animal name, sound it makes
    """
    print(f"""Old MACDONALD had a farm
E-I-E-I-O
And on his farm he had a {animal}
E-I-E-I-O
With a {sound} {sound} here
And a {sound} {sound} there
Here a {sound}, there a {sound}
Everywhere a {sound} {sound}
Old MacDonald had a farm
E-I-E-I-O""")



def main():
    print_verse("cow", "moo")
    print()
    print_verse("pig", "oink")
    print()
    print_verse("duck", "quack")
    print()
    print_verse("horse", "neigh")
    print()
    print_verse("lamb", "baa")


if __name__ == "__main__":
    main()
