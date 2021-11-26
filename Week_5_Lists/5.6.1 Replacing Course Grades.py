"""
COMP.CS.100 Programming 1
Code template for "replacing grades" program
Jani Ollenberg
H288244
"""

# TODO: add the definition for convert_grades here
def convert_grades(grades_list):
    """
    Convert all non-zero grades to 6 meaning pass.
    :param: list of grades
    no return, changes mutable list
    """
    index = -1
    for i in grades_list:
        index += 1
        if i == 0:
            continue
        else:
            grades_list[index] = 6
def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]
    gradeEmpty = []
    convert_grades(gradeEmpty)
    print(gradeEmpty)


if __name__ == "__main__":
    main()
