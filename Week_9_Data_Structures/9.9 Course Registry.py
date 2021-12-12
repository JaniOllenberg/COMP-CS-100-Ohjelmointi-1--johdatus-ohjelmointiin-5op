"""
COMP.CS.100 Programming 1
Registry of courses available at the university.
Jani Ollenberg
H288244
"""

def open_registry():
    """
    Open the courses file and create a registry.
    :return registry: list in dict
    """
    # ask for filename or use default = courses.txt
    filename = input("Enter file name: ") or "courses.txt"

    try:
        data_file = open(filename, mode="r")
    except:
        print("Error opening file!")
        return None

    # read all lines of data_file into a list
    all_lines = data_file.readlines()

    # No need to keep the file open.
    data_file.close()

    # registry of all departments and courses
    registry = {}
    try:
        for line in all_lines:
            # remove end line characters
            line = line.rstrip()

            # split line into parts divided by ";"
            department, course, credits = line.split(";")

            if department not in registry:
                registry[department] = []

            # add course and credits as a list to dictionary of departments
            registry[department].append([course, credits])

        return registry

    except:
        print("Error in file!")
        return None

def ask_command():
    """
    Ask for command and make it into a list of arguments.
    :return command_list: list with command and different arguments
    """

    command = input("Enter command: ")
    command_list = command.split(" ")

    # if command has many words need to join the course name into one string
    if len(command_list) > 2:
        course = " ".join(command_list[2:-1])

        # save command arguments
        command = command_list[0]
        department = command_list[1]
        credits = command_list[-1]

        # Special case to get remove_course() to work properly
        if command == "d" or command == "D":
            course = " ".join(command_list[2:])
            credits = 0

        # remove extra words
        command_list.clear()

        # make the command_list in proper form: command, department, course, credits
        command_list = [command, department, course, credits]

    return command_list

def print_registry(registry):
    """
    Prints the full registry.
    :param registry: list in dict
    """

    print()
    for department in sorted(registry):
        print(f"*{department}*")
        
        # print course name with credit from course list
        for course in sorted(registry[department]):
            print(course[0], ":", course[1], "cr")

def print_department(registry, department):
    """
    Print courses by department.
    :param registry: list in dictionary
    :param department: str name of department
    """

    if department in sorted(registry):
        print(f"\n*{department}*")
        for course in sorted(registry[department]):
            # list in the dict has course name on index 0 and credits in 1
            print(course[0], ":", course[1], "cr")
    else:
        print("Department not found!")
        
def credits_in_department(registry, department):
    """
    Calculate all the credits a department offers.
    :param registry: list of courses and credits in dict
    :param department: str, department to check 
    """

    if department in registry:
        sum = 0
        for course in registry[department]:
            # course[1] contains credits of the course
            sum += int(course[1])

        print(f"Department {department} has to offer {sum} cr.")
    else:
        print("Department not found!")

def add_course(registry, department, course, credits):
    """
    Add course to registry.
    :param registry: list of courses in dictionary
    :param department: str, department to add
    :param course: str course to add
    :param credits: str credits of course
    """

    if department not in registry:
        # Add new department
        registry[department] = []
        print(f"Added department {department} with course {course}")
    else:
        print(f"Added course {course} to department {department}")    

    # Add course to department
    registry[department].append([course, credits])

def remove_course(registry, department, course = 0):
    """
    Remove deparment or course.
    :param registry: list in dict
    :param departmen: str, department to remove
    :param course: str, course to remove, if not passed defaults to 0
    """

    if department not in registry:
        print(f"\nDepartment {department} not found!")
        return

    # remove whole department if no course given
    if course == 0:
        del registry[department]
        print(f"\nDepartment {department} removed.")

    else:
        # Find course in registry and remove
        found = False
        for courses in registry[department]:
            if courses[0] == course:
                found = True
                registry[department].remove(courses)
                print(f"\nDepartment {department} course {course} removed.")
        if found == False:
            print(f"\nCourse {course} from {department} not found!")


def main():
    # Create the registry of all courses
    registry = open_registry()

    # returns None if there's an error
    if registry == None:
        return

    while True:
        # print all command options
        print("\n[A]dd / [C]redits / [D]elete / [P]rint all / p[R]int department \
/ [Q]uit")

        # ask for command
        # returned list contains:
        # command_list[0] = command
        # command_list[1] = department
        # command_list[2] = course
        # command_list[3] = credits
        command_list = ask_command()

        # Action to make with the command

        # Add course
        if command_list[0] == "A" or command_list[0] == "a":
            try:
                add_course(registry, command_list[1], command_list[2], command_list[3])
            except:
                print("Invalid command!")

        # Get credits of department
        elif command_list[0] == "C" or command_list[0] == "c":
            try:
                credits_in_department(registry, command_list[1])
            except:
                print("Need department to check credits from.")

        # Delete department or course
        elif command_list[0] == "D" or command_list[0] == "d":
            try:
                # If command list has department and course
                if len(command_list) == 4:
                    remove_course(registry, command_list[1], command_list[2])
            
                # If command list has only department
                elif len(command_list) == 2:
                    remove_course(registry, command_list[1])
                else:
                    raise Exception    
            except:
                print("Need department or course to remove.")

        # Print all courses
        elif command_list[0] == "P" or command_list[0] == "p":
            print_registry(registry)

        # Print courses in one department
        elif command_list[0] == "R" or command_list[0] == "r":
            try:
                print_department(registry, command_list[1])
            except:
                print("Need department to find courses from.")

        # Quit program.
        elif command_list[0] == "Q" or command_list[0] == "q":
            print("Ending program.")
            return
            
        # Invalid command
        else:
            print("\nInvalid command!")

if __name__ == "__main__":
    main()