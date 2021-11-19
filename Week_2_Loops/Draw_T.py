"""
Draws the letter t based on user's choices.
"""

def main():
    # Print infomation to the user.
    print ("Hello! I draw letter t.")

    # Read the drawing character.
    char = input("Please, enter the drawing character: ")

    # Read the height of the letter and convert the input to an integer.
    height_as_string = input("Please, enter the height of the drawing: ")
    height = int(height_as_string)

    # Draw if the height is odd and greater than two characters.
    if height % 2 == 1 and height > 2:
        # Print the horizontal line. 
        print(height * char)

        # Determine the number of spaces preceding the character of
        # the vertical line.
        nspaces = height // 2

        # Print the vertical line.
        for ind in range(0, height - 1):
            print(nspaces * " " + char)
    # Print the error message.
    else:
        print("Invalid height!")

if __name__ == "__main__":
    main()