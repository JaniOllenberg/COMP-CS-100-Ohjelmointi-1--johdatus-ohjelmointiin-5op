"""
COMP.CS.100 Programming 1
Assignment "Improved Box Printing" code template
Jani Ollenberg
H288244
"""

# TODO: the definition of print_box goes here unless it goes after main.
def print_box(width, height, border_mark='#', inner_mark=' '):
    """
    Print boxes
    :param: width, height, and inner and outer marks with defaults
    :return: none
    """
    for i in range(1, height+1):
        if i == 1 or i == height:
            print(width * border_mark)
        else:
            print(f'{border_mark}{(width-2)*inner_mark}{border_mark}')

def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


# TODO: the definition of print_box could also go here, it is up to you.


if __name__ == "__main__":
    main()
