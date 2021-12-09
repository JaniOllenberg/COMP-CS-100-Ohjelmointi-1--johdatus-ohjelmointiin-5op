"""
COMP.CS.100 Programming 1
Read file and add line numbers to the printout.
Jani Ollenberg
H288244
"""
def main():
    filename = input("Enter the name of the file: ")
    file = open(filename, mode="r")
    line_number = 1
    for line in file:
        line = line.rstrip()
        print(f"{line_number} {line}")
        line_number += 1

if __name__ == "__main__":
    main()