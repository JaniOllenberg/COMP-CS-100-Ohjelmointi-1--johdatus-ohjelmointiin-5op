"""
COMP.CS.100 Programming 1
Code template for geometric patterns.
"""

def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            # Replace this comment and "pass" with your function calls dealing
            # with square.
            pass

        elif answer == "r":
            # Replace this comment and "pass" with your function calls dealing
            # with rectangle.
            pass

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()

def main():
    menu()
    print("Goodbye!")

if __name__ == "__main__":
    main()
