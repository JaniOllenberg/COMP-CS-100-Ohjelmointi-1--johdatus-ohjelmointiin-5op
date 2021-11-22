"""
COMP.CS.100 Programming 1
Print a box with input error checking
Jani Ollenberg
H288244
"""


def print_box(width, height, mark):
    """
    prints a rectancle with desired size and character
    """
    for i in range(height):
        print(mark*width)

def read_input(ask):
    """
    Reads input and asks again if not positive number
    """
    output = int(input(ask))
    while output <= 0:
        output = int(input(ask))
    return output

def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()


    print_box(width, height, mark)


if __name__ == "__main__":
    main()
