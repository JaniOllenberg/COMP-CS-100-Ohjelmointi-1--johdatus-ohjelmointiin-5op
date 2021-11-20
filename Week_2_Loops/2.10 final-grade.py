"""
This course has three different level of the assignments
which also give a student three different types of points:

 -- elementary points (A points)
 -- basic points      (B points)
 -- projects points   (C points)

This program allows user to input those points and after
the input is done, the program tells which final grade
will result based on the sum of the points in each category.

The points of each category don't need to be entered and once.
The program reads the input in a loop and during each round
it inquires the user for a category and points. To make the program
easier to use, the category names are entered as single letters
A, B, and C, which correspond to elementary, basic, and project
categories.

The program stops reading the grades when the user enters
the word "quit" as the category name. After that the final
grade is printed on the screen.
"""

def main():
    QUIT_COMMAND = "quit"

    # The following variables will contain the cumulative
    # sum of the points in each category.
    A_points = 0
    B_points = 0
    C_points = 0

    # category_id must be sneakily initialized into such value,
    # that the while-loop's condition is True on the first time.
    # Otherwise the loop would be skipped altogether.
    category_id = ""
    while category_id != QUIT_COMMAND:
        category_id = input(f"Enter the category letter (or {QUIT_COMMAND}): ")

        # Let's check if the user input is none of the recognized
        # input keywords "A", "B", "C", or QUIT_COMMAND's value ("quit").
        if category_id != "A" and category_id != "B" and category_id != "C" \
           and category_id != QUIT_COMMAND:

            print(f"Error: bad input '{category_id}', try again!")

            # after the error message has been printed, we'll to start
            # the next round of the loop (i.e. jump back to the 'while'-line.
            # In this particular program, the 'continue' command isn't really
            # neccessary, but can you tell why?
            continue

        # If the user input was "A", "B", or "C", the user needs to
        # enter a point value which will be added to the sum variable
        # for that category.
        elif category_id != QUIT_COMMAND:
            points = int(input(f"Enter more category {category_id} points: "))

            if category_id == "A":
                A_points += points

            elif category_id == "B":
                B_points += points

            # Otherwise if can only be "C" category since all other
            # possibilities have allready been checked and taken care of.
            else:
                C_points += points

        # Otherwise nothing needs to be done since the user entered
        # QUIT_COMMAND. Which will cause the loop to end when the
        # condition is checked the next time.
        # This could have been written:
        #
        # else:
        #     pass
        #
        # where 'pass' is the Python's command which doesn't do anything,
        # but it is needed here, since else-branch can't be empty
        # according to Python's syntax rules.  At the end, it is just
        # easier to leave the whole else-branch out.

    # Selecting the correct final grade based on the amout of
    # points in each of the three categories.
    if A_points >= 600 and B_points >= 600 and C_points >= 650:
        final_grade = 5

    elif A_points >= 500 and B_points >= 500 and C_points >= 450:
        final_grade = 4

    elif A_points >= 450 and B_points >= 450 and C_points >= 250:
        final_grade = 3

    elif A_points >= 350 and B_points >= 350 and C_points >= 250:
        final_grade = 2

    elif A_points >= 250 and B_points >= 250 and C_points >= 150:
        final_grade = 1

    else:
        final_grade = 0

    # Let's print all the relevant information on one line.
    print(f"A: {A_points} p. / B: {B_points} p. / C: {C_points} p. / ", end="")
    print(f"Grade:{final_grade}")


if __name__ == "__main__":
    main()
