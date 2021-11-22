"""
COMP.CS.100 Programming 1
Template for task: box printing
Jani Ollenberg
H288244
"""

def print_box(width, height, mark):
    """
    prints a rectancle with desired size and character
    """
    for i in range(height):
        print(mark*width)

def main():
    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
