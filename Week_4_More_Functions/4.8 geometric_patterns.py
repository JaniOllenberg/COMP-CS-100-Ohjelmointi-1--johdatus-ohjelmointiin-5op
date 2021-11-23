"""
COMP.CS.100 Programming 1
Code template for geometric patterns.
Jani Ollenberg
H288244
"""
import math

def circle():
    """
    calculate circle
    :param: none
    :return: none
    """
    radius = ask_side("Enter the circle's radius: ")
    print(f"The circumference is {circumference_circle(radius):.2f}")
    print(f"The surface area is {area(radius):.2f}")

def circumference_circle(radius):
    """
    Calculate circle circumference.
    :param: radius
    :return: circumference
    """
    return math.pi * radius * 2

def area(radius):
    """
    Calculate circle area.
    :param: radius
    :return: area
    """
    return math.pi * radius * radius

def square():
    """
    Calculate square area and circumference
    :param: none
    :return: none
    """
    side = float(ask_side("Enter the length of the square's side: "))
    circumference = 4 * side
    area = side **2
    print(f'The circumference is {circumference:.2f}')
    print(f'The surface area is {area:.2f}')

def rectangle():
    """
    Define rectangle
    :param: none
    :return: none
    """
    side1 = ask_side("Enter the length of the rectangle's side 1: ")
    side2 = ask_side("Enter the length of the rectangle's side 2: ")
    circumference = side1*2 + side2 * 2
    area = side1 * side2
    print(f'The circumference is {circumference:.2f}')
    print(f'The surface area is {area:.2f}')

def ask_side(text):
    """
    ask until positive
    :param text: print text
    :return: float, length of asked side
    """
    side = -1
    while side < 0.00000001:
        side = float(input(text))
    return side


def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            # Replace this comment and "pass" with your function calls dealing
            # with square.
            square()

        elif answer == "r":
            # Replace this comment and "pass" with your function calls dealing
            # with rectangle.
            rectangle()
        
        elif answer == 'c':
            circle()

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
